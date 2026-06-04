"""
feedback_generator.py
---------------------
Generates Socratic feedback using the Gemini API based on
detected cognitive biases from a consultation session.

Key rules:
  - NEVER reveal the correct diagnosis
  - NEVER directly tell the student they were wrong
  - NEVER use the words "bias", "anchoring", "premature closure",
    or "confirmation bias" in the feedback
  - ALWAYS ask Socratic questions that prompt reflection
  - Falls back to rule-based feedback if Gemini call fails

Uses: google-genai library (NEW — not deprecated google-generativeai)
Model: gemini-2.5-flash
Evaluators: medical students (reflected in vocabulary level)
"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

# Initialize Gemini client using NEW google-genai library
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
GEMINI_MODEL = "gemini-2.5-flash"

# System instruction for the Gemini feedback call
_FEEDBACK_SYSTEM_INSTRUCTION = """You are a medical education tutor providing \
Socratic feedback to a medical student after a clinical history-taking exercise \
with a virtual patient. Your role is to prompt deeper reflection.

STRICT RULES:
1. NEVER reveal the correct diagnosis.
2. NEVER say the student was wrong or made an error.
3. NEVER use the words "bias", "anchoring", "premature closure", or \
"confirmation bias" — these are clinical education terms, not words to use \
directly in feedback.
4. ONLY ask open-ended questions that lead the student to reconsider \
their reasoning.
5. Make every question specific to this case and this student's actual \
behaviour during the consultation.
6. Use appropriate clinical vocabulary — the user is a medical student.
7. Keep to exactly 3-4 Socratic questions. One question per line.
8. Do not number the questions. Do not add any preamble or closing statement."""


def generate_feedback(bias_results, session, case_config):
    """
    Main entry point for feedback generation.
    Takes bias detection results and returns Socratic feedback messages.

    Args:
        bias_results (dict): Output from detect_all_biases().
        session (dict): Completed session dict.
        case_config (dict): Case definition from cases.py.

    Returns:
        list: List of feedback message strings (3-4 messages).
              Returns positive feedback if no biases detected.
    """
    # Collect which biases were detected
    detected_biases = []
    for bias_name, result in bias_results.items():
        if result["detected"]:
            detected_biases.append({
                "name": bias_name,
                "score": result["score"],
                "reason": result["reason"],
                "evidence": result["evidence"],
            })

    # If no biases detected, return positive feedback
    if not detected_biases:
        return [
            "Well done — your consultation showed thorough and balanced reasoning.",
            "You covered the key history areas and explored multiple diagnostic "
            "possibilities before reaching a conclusion.",
            "Consider: what single additional investigation or history point "
            "would best confirm your working diagnosis?",
            "Reflect on whether any clue you uncovered could point toward an "
            "alternative diagnosis that should remain on your differential.",
        ]

    # Build the feedback prompt
    prompt = build_feedback_prompt(detected_biases, session, case_config)

    # Call Gemini API — fall back to rule-based if API fails
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=_FEEDBACK_SYSTEM_INSTRUCTION,
                max_output_tokens=400,
                temperature=0.7,
            ),
        )
        feedback_text = response.text

    except Exception as e:
        # Gemini call failed — use rule-based fallback
        print(f"Gemini feedback call failed: {e}")
        feedback_text = build_fallback_feedback(detected_biases, case_config)

    # Split into individual feedback messages (one per line)
    feedback_messages = [
        line.strip()
        for line in feedback_text.split("\n")
        if len(line.strip()) > 10
    ]

    return feedback_messages[:4]  # cap at 4 messages


def build_feedback_prompt(detected_biases, session, case_config):
    """
    Constructs the text prompt sent to Gemini for feedback generation.
    Contains enough context for Gemini to generate relevant Socratic
    questions without revealing the correct diagnosis.

    Args:
        detected_biases (list): List of bias dicts that were detected.
        session (dict): Completed session dict.
        case_config (dict): Case definition including correct_diagnosis
                            (used as context for Gemini but never shown to user).

    Returns:
        str: Complete prompt string ready to send to Gemini.
    """
    # Build bias description section
    bias_descriptions = ""
    for bias in detected_biases:
        bias_descriptions += f"\n- {bias['name'].replace('_', ' ')}: {bias['reason']}"

    # Human-readable topics covered
    topics_str = (
        ", ".join(session.get("topics_covered", [])).replace("_", " ")
        or "none detected"
    )

    prompt = (
        f"A medical student has just completed a virtual patient "
        f"consultation exercise.\n\n"
        f"CASE CONTEXT (do not reveal any of this to the student):\n"
        f"Patient: {case_config['patient_intro']}\n"
        f"Correct diagnosis: {case_config['correct_diagnosis']}\n"
        f"Anchor trap in this case: {case_config['anchor_topic']}\n\n"
        f"STUDENT BEHAVIOUR:\n"
        f"- Total questions asked: {session['question_count']}\n"
        f"- Clinical history topics covered: {topics_str}\n"
        f"- Diagnosis submitted: "
        f"{session.get('diagnosis_submitted', 'not submitted')}\n\n"
        f"REASONING PATTERNS DETECTED:\n"
        f"{bias_descriptions}\n\n"
        f"TASK:\n"
        f"Generate 3-4 Socratic questions to help this medical student reflect "
        f"on their clinical reasoning. Do not reveal the correct diagnosis. "
        f"Do not say the student was wrong. Do not use bias terminology. "
        f"Ask questions that naturally lead the student to reconsider what they "
        f"may have missed. Make each question specific to this patient's "
        f"presentation and this student's actual behaviour during the "
        f"consultation. One question per line, no numbering."
    )

    return prompt


def build_fallback_feedback(detected_biases, case_config):
    """
    Returns rule-based feedback if Gemini API call fails.
    Ensures system gives useful output even without internet connection.

    Args:
        detected_biases (list): List of bias dicts that were detected.
        case_config (dict): Case definition from cases.py.

    Returns:
        str: Newline-separated feedback messages as a single string.
    """
    messages = []

    for bias in detected_biases:

        if bias["name"] == "anchoring":
            messages.append(
                f"You focused significantly on {case_config['anchor_topic']} "
                f"as a cause — what other diagnoses could produce this exact "
                f"constellation of symptoms?"
            )
            messages.append(
                "Did you ask about all the patient's regular medications? "
                "Pharmacological causes are among the most commonly missed "
                "aetiologies in primary care presentations."
            )

        elif bias["name"] == "premature_closure":
            messages.append(
                "You reached a diagnosis relatively early in the history. "
                "What additional clinical information might shift your "
                "differential diagnosis or change your management plan?"
            )
            if bias["evidence"]:
                missed = bias["evidence"][0]
                messages.append(
                    f"You did not ask about {missed}. "
                    f"How might that information affect your assessment "
                    f"of this patient?"
                )

        elif bias["name"] == "confirmation_bias":
            messages.append(
                "Were there questions you decided not to ask because you "
                "already felt confident in your working diagnosis?"
            )
            messages.append(
                "What single piece of clinical information, if present, "
                "would make you completely reconsider this diagnosis — "
                "and did you specifically ask about it?"
            )

    return "\n".join(messages[:4])
