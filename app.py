"""
app.py
------
Main Flask application. Defines all URL routes for the web app.

Routes:
  GET  /                  → case selection page
  GET  /start/<case_id>   → begin a consultation for a specific case
  POST /chat              → user sends message, get patient reply
  POST /conclude          → user submits diagnosis, get bias feedback

Uses:
  - cases.py for case definitions
  - session_tracker.py for tracking user behavior
  - bias_detector.py for detecting cognitive biases
  - feedback_generator.py for generating Socratic feedback
  - Gemini API (gemini-2.5-flash) for virtual patient responses

IMPORTANT: Uses NEW google-genai library (not deprecated google-generativeai)
  Correct: from google import genai
  Wrong:   import google.generativeai as genai
"""

import os
import json
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
app.secret_key = os.urandom(24)

# Initialize Gemini client — NEW google-genai library
# client is created once at startup and reused for all requests
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
GEMINI_MODEL = "gemini-2.5-flash"


@app.route("/")
def index():
    """
    Home page — shows all available cases for the user to choose from.
    Renders templates/index.html with the list of cases.
    """
    pass  # TODO Day 6: implement this


@app.route("/start/<case_id>")
def start_case(case_id):
    """
    Begins a consultation for a specific case.
    Creates a fresh session and renders the chat interface.

    URL example: /start/case_1
    case_id is captured from the URL automatically by Flask.
    """
    pass  # TODO Day 6: implement this


@app.route("/chat", methods=["POST"])
def chat():
    """
    Receives a user message and returns the virtual patient's reply.
    Updates session tracking on every call.

    Expects JSON body: {"message": "Does the pain go to your arm?"}
    Returns JSON: {"response": "No, just in my chest.", "question_count": 3}
    """
    pass  # TODO Day 8: implement with real Gemini call


@app.route("/conclude", methods=["POST"])
def conclude():
    """
    Receives the user's final diagnosis and returns bias feedback.
    Runs bias detection then generates Socratic feedback via Gemini.

    Expects JSON body: {"diagnosis": "Myocardial infarction"}
    Returns JSON: {
        "diagnosis_given": str,
        "questions_asked": int,
        "biases_detected": dict,
        "feedback_messages": list,
        "session_summary": dict
    }
    """
    pass  # TODO Day 11: implement this


@app.route("/save_session", methods=["POST"])
def save_session():
    """
    Saves the completed session data as a JSON file in sessions/ folder.
    Called automatically after /conclude completes.
    This creates the research data used in the evaluation phase.

    Session files are named: case1_YYYYMMDD_HHMMSS.json
    """
    pass  # TODO Day 11: implement this


if __name__ == "__main__":
    # debug=True: Flask restarts automatically when you save a file
    # port=5000: app runs at http://localhost:5000
    # Never use debug=True in production
    app.run(debug=True, port=5000)