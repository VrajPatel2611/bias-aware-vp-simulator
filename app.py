"""
app.py
------
Main Flask application. Defines all URL routes for the web app.

Routes:
  GET  /                  → case selection page
  GET  /start/<case_id>   → begin a consultation for a specific case
  POST /chat              → user sends message, get patient reply
  POST /conclude          → user submits diagnosis, get bias feedback
  POST /save_session      → thin wrapper (session saved inside /conclude)

Session storage:
  Flask session cookie holds only a session_id UUID.
  Full session data (conversation history, tracking) lives in SESSION_STORE,
  an in-memory dict keyed by session_id. This avoids cookie size limits.

Uses:
  - cases.py             for case definitions
  - session_tracker.py   for tracking user behaviour
  - bias_detector.py     for detecting cognitive biases
  - feedback_generator.py for generating Socratic feedback
  - Gemini API (gemini-2.5-flash) for virtual patient responses

IMPORTANT: Uses NEW google-genai library (not deprecated google-generativeai)
  Correct: from google import genai
  Wrong:   import google.generativeai as genai
"""

import os
import json
import uuid
from datetime import datetime

from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv
from google import genai
from google.genai import types

from cases import get_all_cases, get_case
from session_tracker import create_session, update_session, get_session_summary
from bias_detector import detect_all_biases
from feedback_generator import generate_feedback

load_dotenv()

app = Flask(__name__)
# secret_key signs the Flask session cookie
app.secret_key = os.environ.get("FLASK_SECRET_KEY", os.urandom(24))

# Initialize Gemini client — NEW google-genai library
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
GEMINI_MODEL = "gemini-2.5-flash"

# ── Server-side session store ─────────────────────────────────────────
# Stores full session state in memory to avoid cookie size limits.
# Cleared on server restart — fine for this prototype.
# Format: {session_id: {"session_data": {...}, "conversation": [...]}}
SESSION_STORE = {}


# ── Routes ────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """
    Home page — shows all available cases for the user to choose from.
    Renders templates/index.html with the list of cases.
    """
    cases = get_all_cases()
    return render_template("index.html", cases=cases)


@app.route("/start/<case_id>")
def start_case(case_id):
    """
    Begins a consultation for a specific case.
    Creates a fresh session and renders the chat interface.

    URL example: /start/case_1
    """
    case = get_case(case_id)
    if not case:
        return "Case not found.", 404

    # Create a new server-side session
    session_id = str(uuid.uuid4())
    session_data = create_session(case_id)

    SESSION_STORE[session_id] = {
        "session_data": session_data,
        "conversation": [],  # list of {"role": "user"/"model", "content": str}
    }

    # Store only session_id in Flask cookie
    session["session_id"] = session_id
    session["case_id"] = case_id

    return render_template("chat.html", case=case)


@app.route("/chat", methods=["POST"])
def chat():
    """
    Receives a user message and returns the virtual patient's reply.
    Updates session tracking on every call.

    Expects JSON body: {"message": "Does the pain go to your arm?"}
    Returns JSON:      {"response": "No, just in my chest.", "question_count": 3}
    """
    session_id = session.get("session_id")
    case_id = session.get("case_id")

    if not session_id or session_id not in SESSION_STORE:
        return jsonify({
            "error": "No active session. Please go back and select a case."
        }), 400

    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Empty message."}), 400

    store = SESSION_STORE[session_id]
    session_data = store["session_data"]
    conversation = store["conversation"]
    case = get_case(case_id)

    # Build Gemini conversation history in correct format
    # NEW library uses role="model" (not "assistant")
    gemini_contents = []
    for msg in conversation:
        role = "user" if msg["role"] == "user" else "model"
        gemini_contents.append(
            types.Content(
                role=role,
                parts=[types.Part(text=msg["content"])],
            )
        )

    # Append the new user message
    gemini_contents.append(
        types.Content(
            role="user",
            parts=[types.Part(text=user_message)],
        )
    )

    # Call Gemini with the patient system prompt
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=gemini_contents,
            config=types.GenerateContentConfig(
                system_instruction=case["system_prompt"],
                max_output_tokens=200,
                temperature=0.7,
            ),
        )
        patient_reply = response.text

    except Exception as e:
        return jsonify({"error": f"Patient response error: {str(e)}"}), 500

    # Update session tracking
    update_session(session_data, user_message)

    # Append to conversation history
    conversation.append({"role": "user", "content": user_message})
    conversation.append({"role": "model", "content": patient_reply})

    return jsonify({
        "response": patient_reply,
        "question_count": session_data["question_count"],
    })


@app.route("/conclude", methods=["POST"])
def conclude():
    """
    Receives the user's final diagnosis and returns bias feedback.
    Runs bias detection then generates Socratic feedback via Gemini.
    Also saves the completed session as a JSON file in sessions/.

    Expects JSON body: {"diagnosis": "Myocardial infarction"}
    Returns JSON: {
        "diagnosis_given": str,
        "questions_asked": int,
        "biases_detected": dict,
        "feedback_messages": list,
        "session_summary": dict
    }
    """
    session_id = session.get("session_id")
    case_id = session.get("case_id")

    if not session_id or session_id not in SESSION_STORE:
        return jsonify({"error": "No active session."}), 400

    data = request.get_json(silent=True) or {}
    diagnosis = data.get("diagnosis", "").strip()
    if not diagnosis:
        return jsonify({"error": "No diagnosis provided."}), 400

    store = SESSION_STORE[session_id]
    session_data = store["session_data"]
    case = get_case(case_id)

    # Record diagnosis and end time
    session_data["diagnosis_submitted"] = diagnosis
    session_data["end_time"] = datetime.utcnow().isoformat()

    # Run bias detection
    bias_results = detect_all_biases(session_data, case)

    # Generate Socratic feedback
    feedback_messages = generate_feedback(bias_results, session_data, case)

    # Build session summary
    summary = get_session_summary(session_data, case)

    # Save session JSON to sessions/ folder
    _save_session_file(
        session_id, case_id, case, session_data, bias_results, feedback_messages
    )

    return jsonify({
        "diagnosis_given": diagnosis,
        "questions_asked": session_data["question_count"],
        "biases_detected": bias_results,
        "feedback_messages": feedback_messages,
        "session_summary": summary,
    })


@app.route("/save_session", methods=["POST"])
def save_session_route():
    """
    Thin wrapper — sessions are saved automatically inside /conclude.
    Kept for completeness and potential external use.
    """
    return jsonify({"status": "Sessions are saved automatically on /conclude."})


# ── Helpers ───────────────────────────────────────────────────────────

def _save_session_file(
    session_id, case_id, case, session_data, bias_results, feedback_messages
):
    """
    Saves the completed session as a JSON file in the sessions/ folder.
    Filenames: case1_YYYYMMDD_HHMMSS.json
    These files are the research data used in the evaluation phase.
    Silently skips if the folder is not writable.
    """
    try:
        os.makedirs("sessions", exist_ok=True)
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        filename = f"sessions/{case_id}_{timestamp}.json"

        log = {
            "session_id": f"{case_id}_{timestamp}",
            "case_id": case_id,
            "case_title": case["title"],
            "correct_diagnosis": case["correct_diagnosis"],
            "start_time": session_data.get("start_time"),
            "end_time": session_data.get("end_time"),
            "question_count": session_data["question_count"],
            "questions_asked": session_data["questions_asked"],
            "topics_covered": session_data["topics_covered"],
            "early_diagnosis": session_data.get("early_diagnosis"),
            "diagnosis_submitted": session_data["diagnosis_submitted"],
            "biases_detected": bias_results,
            "feedback_given": feedback_messages,
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(log, f, indent=2, ensure_ascii=False)

        print(f"Session saved: {filename}")

    except Exception as e:
        print(f"Warning: Could not save session file: {e}")


# ── Entry point ───────────────────────────────────────────────────────

if __name__ == "__main__":
    # debug=True: Flask restarts automatically when you save a file
    # Never use debug=True in production
    app.run(debug=True, port=5000)
