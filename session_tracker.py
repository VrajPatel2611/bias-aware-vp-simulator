"""
session_tracker.py
------------------
Tracks everything the user does during one consultation session.
Records: questions asked, topics covered, question count, diagnosis.

Called by: app.py on every POST /chat request
Uses: TOPIC_KEYWORDS dictionary for topic detection
Returns: updated session dict stored in Flask session object

NOTE: The real logic for all functions below is documented in
docs/pseudocode.md — read that before implementing on Day 9.
"""

# ── Topic keyword lookup table ──────────────────────────────────────
# Maps topic category names to lists of trigger words.
# These category names match the required_topics lists in cases.py.
# When a user message contains any keyword from a category,
# that topic is marked as covered in the session.

TOPIC_KEYWORDS = {
    "pain_character": [
        "burning", "crushing", "sharp", "dull", "aching",
        "character", "describe", "feel like", "what kind",
        "pressure", "tight", "stabbing"
    ],
    "meal_relationship": [
        "meal", "food", "eating", "after eating", "diet",
        "drink", "spicy", "coffee", "fasting", "empty stomach"
    ],
    "radiation": [
        "radiate", "spread", "arm", "jaw", "shoulder",
        "neck", "anywhere else", "go to", "move to"
    ],
    "associated_symptoms": [
        "breathless", "nausea", "sweat", "dizzy", "fever",
        "vomit", "other symptoms", "weakness", "fatigue"
    ],
    "medications": [
        "medication", "medicine", "drug", "tablet", "pill",
        "taking", "prescribed", "supplements", "painkillers", "regular"
    ],
    "family_history": [
        "family", "father", "mother", "parent", "sibling",
        "hereditary", "runs in family", "relative", "grandfather"
    ],
    "duration_pattern": [
        "how long", "when did", "since when", "started",
        "days", "weeks", "months", "constant", "comes and goes"
    ],
    "relieving_factors": [
        "better", "worse", "relief", "helps", "aggravate",
        "trigger", "lying down", "sitting up", "activity"
    ],
    "headache_character": [
        "throbbing", "pressure", "tight", "band", "one side",
        "both sides", "where", "location", "pulsating", "pounding"
    ],
    "timing_pattern": [
        "morning", "night", "evening", "after", "before",
        "always", "sometimes", "pattern", "time of day"
    ],
    "visual_symptoms": [
        "vision", "blurry", "blur", "spots", "floaters",
        "eyes", "visual", "aura", "light", "sight"
    ],
    "BP_awareness": [
        "blood pressure", "BP", "checked", "measured",
        "monitor", "high pressure", "hypertension"
    ],
    "lifestyle": [
        "sleep", "diet", "water", "hydration", "caffeine",
        "alcohol", "exercise", "routine", "lifestyle"
    ],
    "stress_assessment": [
        "stress", "pressure", "deadline", "recently",
        "changed", "happened", "difficult", "worry", "anxious"
    ],
    "onset_timing": [
        "when", "how long", "started", "sudden", "gradual",
        "yesterday", "this morning", "last week", "recent"
    ],
    "baseline_cognition": [
        "normal", "usual", "before", "last week",
        "always like this", "change", "different", "baseline"
    ],
    "fever": [
        "fever", "temperature", "hot", "chills",
        "sweating", "warm", "shivering", "unwell"
    ],
    "urinary_symptoms": [
        "urinate", "urine", "pee", "toilet", "frequency",
        "burning", "colour", "smell", "waterworks"
    ],
    "recent_illness": [
        "recently", "fell", "hospital", "unwell",
        "illness", "injury", "change", "last few days"
    ],
    "focal_neuro_signs": [
        "weakness", "arm", "leg", "face", "drooping",
        "speech", "slurred", "one side", "paralysis"
    ],
    "hydration": [
        "eating", "drinking", "water", "food", "appetite",
        "fluids", "dehydrated", "thirsty"
    ],
    "mood_vs_physical": [
        "mood", "sad", "hopeless", "happy", "emotional",
        "crying", "enjoying", "interests", "depression", "mentally"
    ],
    "weight_change_pattern": [
        "eating", "food", "appetite", "more", "less",
        "same", "calories", "portion", "hungry"
    ],
    "temperature_tolerance": [
        "cold", "temperature", "always cold", "chilly",
        "layers", "warm", "heating", "feel cold"
    ],
    "bowel_habits": [
        "bowel", "constipated", "constipation", "toilet",
        "frequency", "going less", "difficulty", "sluggish"
    ],
    "hair_skin_changes": [
        "hair", "falling out", "hair loss", "skin", "dry",
        "brittle", "nails", "rough", "texture"
    ],
    "family_thyroid_history": [
        "family", "thyroid", "mother", "father", "sister",
        "relative", "thyroid condition", "underactive", "levothyroxine"
    ],
    "menstrual_changes": [
        "period", "menstrual", "cycle", "regular", "heavy",
        "irregular", "missed", "monthly", "flow"
    ],
    "energy_time_pattern": [
        "morning", "afternoon", "all day", "energy level",
        "when tired", "time of day", "most tired"
    ],
    "fever_infection_signs": [
        "fever", "temperature", "runny nose", "sore throat",
        "ear", "tonsils", "sick", "ill", "unwell"
    ],
    "symptom_timing_pattern": [
        "morning", "night", "evening", "worse when",
        "when bad", "timing", "sleeping", "waking"
    ],
    "exercise_trigger": [
        "exercise", "running", "sport", "PE", "playing",
        "after exercise", "active", "breathless", "exertion"
    ],
    "cold_air_trigger": [
        "cold air", "outside", "weather", "cold", "winter",
        "wind", "going out", "temperature changes"
    ],
    "duration_recurrence": [
        "before", "first time", "happened before", "previous",
        "recurring", "again", "history of", "ever had"
    ],
    "family_atopy_history": [
        "asthma", "allergy", "eczema", "hay fever",
        "atopy", "family", "inhaler", "allergic"
    ],
    "school_sport_impact": [
        "school", "missing", "PE", "sport", "activity",
        "playing", "limited", "avoiding", "stopped"
    ],
}


# ── Functions ────────────────────────────────────────────────────────

def create_session(case_id):
    """
    Creates a fresh session dictionary for a new consultation.
    Called in app.py when user starts a new case via /start/<case_id>.

    Args:
        case_id (str): e.g. "case_1"

    Returns:
        dict: Empty session with all tracking fields initialized.
    """
    pass  # TODO Day 9: implement this


def update_session(session, user_message):
    """
    Updates session after every user message.
    Increments question count, extracts topics, checks for early diagnosis.

    Args:
        session (dict): Current session dict from Flask session storage.
        user_message (str): The raw text the user just sent.

    Returns:
        dict: Updated session dict.
    """
    pass  # TODO Day 9: implement this


def extract_topics(user_message):
    """
    Scans a user message for keywords matching clinical topic categories.
    Uses the TOPIC_KEYWORDS dictionary above.

    Args:
        user_message (str): Raw text from user.

    Returns:
        list: Topic category names found in the message.
              e.g. ["meal_relationship", "medications"]
    """
    pass  # TODO Day 9: implement this


def get_session_summary(session, case_config):
    """
    Returns a readable summary dict for the post-session display screen.
    Used to show the user what they covered and missed.

    Args:
        session (dict): Completed session dict.
        case_config (dict): The case definition from cases.py.

    Returns:
        dict: Summary with coverage stats and missed topics.
    """
    pass  # TODO Day 9: implement this