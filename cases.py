"""
cases.py
--------
Defines all 5 clinical case configurations for the virtual patient
simulator. Each case contains the patient persona, Gemini system
prompt, correct diagnosis, and bias detection configuration.

This file is the Python translation of docs/cases_design.md.
Never change this file without first updating cases_design.md.

Case list:
  case_1: Ramesh Kumar, 48M — Chest pain — GERD vs Cardiac anchor
  case_2: Priya Sharma, 28F — Headache — Hypertension vs Stress anchor
  case_3: Gopal Mehta, 74M — Confusion — UTI vs Stroke/Dementia anchor
  case_4: Meera Patel, 35F — Fatigue — Hypothyroidism vs Depression anchor
  case_5: Arjun Shah, 10M — Wheeze — Asthma vs Infection anchor
"""

# All 5 cases are defined in this dictionary.
# Each case_id maps to a complete configuration dict.
# On Day 5 you will fill in every field with real content.
# Today the structure exists but values are placeholders.

CASES = {
    "case_1": {
        "id": "case_1",
        "title": "The Chest Pain Trap",
        "patient_intro": "",       # TODO Day 5: fill from cases_design.md
        "system_prompt": "",       # TODO Day 5: write full Gemini prompt
        "correct_diagnosis": "",   # TODO Day 5: fill in
        "anchor_topic": "",        # TODO Day 5: fill in
        "anchor_keywords": [],     # TODO Day 5: copy from cases_design.md
        "alternative_topics": [],  # TODO Day 5: copy from cases_design.md
        "required_topics": [],     # TODO Day 5: copy from cases_design.md
        "minimum_questions": 0,    # TODO Day 5: fill in
        "contradictory_clues": [], # TODO Day 5: copy from cases_design.md
    },
    "case_2": {
        "id": "case_2",
        "title": "The Headache That Is Not Stress",
        "patient_intro": "",
        "system_prompt": "",
        "correct_diagnosis": "",
        "anchor_topic": "",
        "anchor_keywords": [],
        "alternative_topics": [],
        "required_topics": [],
        "minimum_questions": 0,
        "contradictory_clues": [],
    },
    "case_3": {
        "id": "case_3",
        "title": "The Confused Elderly Man",
        "patient_intro": "",
        "system_prompt": "",
        "correct_diagnosis": "",
        "anchor_topic": "",
        "anchor_keywords": [],
        "alternative_topics": [],
        "required_topics": [],
        "minimum_questions": 0,
        "contradictory_clues": [],
    },
    "case_4": {
        "id": "case_4",
        "title": "The Tired Teacher",
        "patient_intro": "",
        "system_prompt": "",
        "correct_diagnosis": "",
        "anchor_topic": "",
        "anchor_keywords": [],
        "alternative_topics": [],
        "required_topics": [],
        "minimum_questions": 0,
        "contradictory_clues": [],
    },
    "case_5": {
        "id": "case_5",
        "title": "The Wheezing Child",
        "patient_intro": "",
        "system_prompt": "",
        "correct_diagnosis": "",
        "anchor_topic": "",
        "anchor_keywords": [],
        "alternative_topics": [],
        "required_topics": [],
        "minimum_questions": 0,
        "contradictory_clues": [],
    },
}


def get_case(case_id):
    """
    Returns a single case config dict by ID.

    Args:
        case_id (str): e.g. "case_1"

    Returns:
        dict: Full case config, or None if case_id not found.
    """
    return CASES.get(case_id)


def get_all_cases():
    """
    Returns a lightweight list of all cases for the selection screen.
    Only includes id, title, and patient_intro — not the full config.

    Returns:
        list: [{"id": ..., "title": ..., "intro": ...}, ...]
    """
    return [
        {
            "id": case_id,
            "title": data["title"],
            "intro": data["patient_intro"]
        }
        for case_id, data in CASES.items()
    ]