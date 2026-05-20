"""
feedback_generator.py
---------------------
Generates Socratic feedback using the Gemini API based on
detected cognitive biases from a consultation session.

Key rules:
  - NEVER reveal the correct diagnosis
  - NEVER directly tell the student they were wrong
  - ALWAYS ask Socratic questions that prompt reflection
  - Falls back to rule-based feedback if Gemini call fails

Uses: google-genai library (NEW — not deprecated google-generativeai)
Model: gemini-2.5-flash
Called by: app.py after detect_all_biases() in POST /conclude route

NOTE: Full logic documented in docs/pseudocode.md Section MODULE 3.
"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

# Initialize Gemini client using NEW google-genai library
# This is the correct way — NOT genai.configure() which is deprecated
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
GEMINI_MODEL = "gemini-2.5-flash"


def generate_feedback(bias_results, session, case_config):
    """
    Main entry point for feedback generation.
    Takes bias detection results and returns Socratic feedback messages.

    Args:
        bias_results (dict): Output from detect_all_biases().
        session (dict): Completed session dict.
        case_config (dict): Case definition from cases.py.

    Returns:
        list: List of feedback message strings (max 4 messages).
              Returns positive feedback if no biases detected.
    """
    pass  # TODO Day 11: implement this


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
    pass  # TODO Day 11: implement this


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
    pass  # TODO Day 11: implement this