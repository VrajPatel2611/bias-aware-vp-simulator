# Bias-Aware Virtual Patient Simulator

A chatbot-based clinical training tool that simulates patient consultations
and detects cognitive biases in the user's reasoning process, providing
targeted Socratic feedback.

## Project
B.Tech Summer Internship 2026 — DA-IICT
Student: Roll No. 202301408 | Mentor: Abhishek Gupta
Area of Interest: Machine Learning

## What It Does
Users act as a clinician and ask questions to a virtual patient.
The system tracks their reasoning behavior and detects:
- **Anchoring bias** — fixating on the most obvious symptom
- **Premature closure** — concluding before thorough workup
- **Confirmation bias** — only seeking confirming evidence

After the user submits a diagnosis, the system generates Socratic
feedback using Gemini AI to prompt reflection on reasoning errors.

## Tech Stack
- Python 3.11 + Flask (backend)
- Google Gemini 2.5 Flash via google-genai library (virtual patient + feedback)
- HTML / CSS / JavaScript (frontend — no frameworks)
- Rule-based bias detection engine

## Setup
```bash
git clone https://github.com/YOUR_USERNAME/bias-aware-vp-simulator
cd bias-aware-vp-simulator
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Add your Gemini API key to .env
python app.py
# Open http://localhost:5000
```

## Project Structure

app.py                  Flask routes — main entry point
cases.py                5 clinical case definitions
session_tracker.py      Tracks user questions and topics
bias_detector.py        Rule-based bias detection engine
feedback_generator.py   Socratic feedback via Gemini API
templates/              HTML pages (index, chat, feedback)
static/                 CSS and JavaScript
sessions/               Session JSON logs (research data)
docs/                   Design documents and references

## Cases
1. Ramesh Kumar (48M) — Chest pain → GERD vs Cardiac anchor
2. Priya Sharma (28F) — Headache → Hypertension vs Stress anchor
3. Gopal Mehta (74M) — Confusion → UTI vs Stroke/Dementia anchor
4. Meera Patel (35F) — Fatigue → Hypothyroidism vs Depression anchor
5. Arjun Shah (10M) — Wheeze → Asthma vs Infection anchor