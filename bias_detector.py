"""
bias_detector.py
----------------
Detects three cognitive biases from a completed consultation session.
Called by app.py after user submits diagnosis via POST /conclude.

Three bias types detected:
  1. Anchoring — fixating on the most obvious symptom
  2. Premature closure — concluding before thorough workup
  3. Confirmation bias — only seeking confirming evidence

NOTE: Full detection logic is documented in docs/pseudocode.md.
Read Section "MODULE 2: bias_detector.py" before implementing Day 10.
"""


def detect_all_biases(session, case_config):
    """
    Main entry point. Runs all three bias detectors.
    This is the only function app.py calls directly from this module.

    Args:
        session (dict): Completed session from session_tracker.
        case_config (dict): Case definition from cases.py.

    Returns:
        dict: {
            "anchoring": {detected, score, reason, evidence},
            "premature_closure": {detected, score, reason, evidence},
            "confirmation_bias": {detected, score, reason, evidence}
        }
    """
    pass  # TODO Day 10: implement this


def detect_anchoring(session, case_config):
    """
    Checks if user over-focused on the anchor topic without
    exploring alternative explanations.

    Uses two rules from pseudocode.md:
      Rule A1: More than 60% of questions about anchor topic
      Rule A2: Asked 3+ anchor questions but zero alternative questions

    Args:
        session (dict): Session dict with questions_asked list.
        case_config (dict): Has anchor_keywords and alternative_topics.

    Returns:
        dict: {detected: bool, score: float 0-1, reason: str, evidence: list}
    """
    pass  # TODO Day 10: implement this


def detect_premature_closure(session, case_config):
    """
    Checks if user concluded before a thorough workup.

    Uses two rules from pseudocode.md:
      Rule P1: Fewer questions than minimum_questions threshold
      Rule P2: Fewer than 60% of required_topics covered

    Args:
        session (dict): Session dict with question_count and topics_covered.
        case_config (dict): Has minimum_questions and required_topics.

    Returns:
        dict: {detected: bool, score: float 0-1, reason: str, evidence: list}
              evidence contains list of missed topic names
    """
    pass  # TODO Day 10: implement this


def detect_confirmation_bias(session, case_config):
    """
    Checks if user only sought confirming evidence for their
    initial assumption and never explored contradictory information.

    Uses two rules from pseudocode.md:
      Rule C1: Submitted anchor diagnosis but explored 0 contradictory clues
      Rule C2: Explored fewer than 25% of contradictory clues overall

    Args:
        session (dict): Session dict with questions_asked and diagnosis_submitted.
        case_config (dict): Has contradictory_clues and anchor_keywords.

    Returns:
        dict: {detected: bool, score: float 0-1, reason: str, evidence: list}
    """
    pass  # TODO Day 10: implement this