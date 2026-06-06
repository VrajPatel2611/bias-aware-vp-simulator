"""
investigations_master.py
------------------------
Universal investigation list — identical for every case.

Every test a doctor might order is here, organised by clinical group.
The same list appears on every case's Investigations tab.

HOW RESULTS WORK:
  1. Student clicks a test.
  2. If the test key exists in case.investigations → return that
     case-specific result (may be normal OR abnormal).
  3. Otherwise → return the default_result here (always normal/unremarkable).

WHY THIS MATTERS EDUCATIONALLY:
  - Students cannot see which tests are "relevant" from the UI — they
    must know from clinical reasoning.
  - Over-ordering gets tracked and flagged in feedback.
  - Ordering the wrong key test returns a realistic normal result (real
    medicine also gives normal results when you're chasing the wrong Dx).

GROUPS (collapsible in the UI):
  1. Routine Bloods
  2. Specialist Bloods & Markers
  3. Hormones, Autoimmune & Metabolic
  4. Blood Gas & Lactate
  5. Microbiology & Infection
  6. Urine Tests
  7. Cardiac Investigations
  8. Imaging — X-ray & CT
  9. Imaging — MRI & Ultrasound
  10. Respiratory & Lung Function
  11. GI Procedures
  12. Neurology
  13. Clinical Decision Tools
"""

# ── Master Investigation List ─────────────────────────────────────────
# Format: key → {label, group, default_result}
# key is the same string used in case.investigations dicts.
# default_result is a realistic NORMAL result for this test.

INVESTIGATIONS_MASTER = {

    # ── 1. ROUTINE BLOODS ────────────────────────────────────────────
    "fbc": {
        "label": "Full blood count (FBC)",
        "group": "Routine Bloods",
        "default_result": (
            "Hb 140 g/L · MCV 88 fL · WCC 7.2 × 10⁹/L · Neutrophils 4.8 · "
            "Lymphocytes 2.1 · Plt 275 × 10⁹/L — all within normal limits."
        ),
    },
    "ue": {
        "label": "Urea & electrolytes / Renal function",
        "group": "Routine Bloods",
        "default_result": (
            "Na 138 mmol/L · K 4.0 mmol/L · Urea 5.1 mmol/L · "
            "Creatinine 82 µmol/L · eGFR > 90 mL/min — within normal limits."
        ),
    },
    "lft": {
        "label": "Liver function tests (LFTs)",
        "group": "Routine Bloods",
        "default_result": (
            "Bilirubin 11 µmol/L · ALT 28 U/L · ALP 72 U/L · GGT 34 U/L · "
            "Albumin 42 g/L · Total protein 74 g/L — within normal limits."
        ),
    },
    "amylase": {
        "label": "Serum amylase",
        "group": "Routine Bloods",
        "default_result": "44 U/L — within normal limits (< 100 U/L).",
    },
    "lipase": {
        "label": "Serum lipase",
        "group": "Routine Bloods",
        "default_result": "38 U/L — within normal limits (< 60 U/L).",
    },
    "lipids": {
        "label": "Lipid profile (fasting)",
        "group": "Routine Bloods",
        "default_result": (
            "Total cholesterol 4.8 mmol/L · LDL 2.8 · HDL 1.4 · "
            "Triglycerides 1.2 — within recommended targets."
        ),
    },
    "glucose": {
        "label": "Blood glucose (capillary / fasting)",
        "group": "Routine Bloods",
        "default_result": "5.2 mmol/L — normal (fasting reference 3.9–6.0 mmol/L).",
    },
    "hba1c": {
        "label": "HbA1c (glycated haemoglobin)",
        "group": "Routine Bloods",
        "default_result": (
            "36 mmol/mol (5.5%) — normal (< 48 mmol/mol). "
            "No evidence of chronic hyperglycaemia."
        ),
    },
    "crp": {
        "label": "CRP (C-reactive protein)",
        "group": "Routine Bloods",
        "default_result": "3 mg/L — within normal limits (< 5 mg/L).",
    },
    "esr": {
        "label": "ESR (erythrocyte sedimentation rate)",
        "group": "Routine Bloods",
        "default_result": "14 mm/hr — within normal limits.",
    },
    "coag": {
        "label": "Coagulation screen (PT, APTT, INR, fibrinogen)",
        "group": "Routine Bloods",
        "default_result": (
            "INR 1.0 · APTT 28 s · PT 12 s · Fibrinogen 3.2 g/L — "
            "coagulation within normal limits."
        ),
    },
    "bone_profile": {
        "label": "Bone profile (calcium, phosphate, ALP)",
        "group": "Routine Bloods",
        "default_result": (
            "Adjusted calcium 2.34 mmol/L (normal) · "
            "Phosphate 1.1 mmol/L (normal) · ALP 72 U/L — within normal limits."
        ),
    },
    "urate": {
        "label": "Serum urate / uric acid",
        "group": "Routine Bloods",
        "default_result": "310 µmol/L — within normal limits (< 420 µmol/L).",
    },
    "ck": {
        "label": "Creatine kinase (CK / CPK)",
        "group": "Routine Bloods",
        "default_result": "82 U/L — within normal limits (< 170 U/L).",
    },
    "ldh": {
        "label": "Lactate dehydrogenase (LDH)",
        "group": "Routine Bloods",
        "default_result": "188 U/L — within normal limits (< 250 U/L).",
    },

    # ── 2. SPECIALIST BLOODS & CARDIAC MARKERS ───────────────────────
    "troponin": {
        "label": "High-sensitivity Troponin I (serial: 0 h + 3 h)",
        "group": "Specialist Bloods & Markers",
        "default_result": (
            "Troponin I at 0 h: 3 ng/L (reference < 14 ng/L) — negative. "
            "Troponin I at 3 h: 3 ng/L — negative. Delta troponin: 0. "
            "ACS effectively excluded on serial troponins."
        ),
    },
    "bnp": {
        "label": "BNP / NT-proBNP",
        "group": "Specialist Bloods & Markers",
        "default_result": (
            "BNP 42 pg/mL — normal (< 100 pg/mL). "
            "No biochemical evidence of cardiac failure."
        ),
    },
    "d_dimer": {
        "label": "D-dimer",
        "group": "Specialist Bloods & Markers",
        "default_result": (
            "D-dimer < 500 ng/mL — negative. "
            "No biochemical evidence of thromboembolism. "
            "Note: D-dimer is sensitive but not specific; interpret in clinical context."
        ),
    },
    "lactate": {
        "label": "Serum lactate",
        "group": "Specialist Bloods & Markers",
        "default_result": "1.1 mmol/L — normal (< 2.0 mmol/L). No evidence of tissue hypoperfusion.",
    },
    "blood_ketones": {
        "label": "Blood ketones (beta-hydroxybutyrate)",
        "group": "Specialist Bloods & Markers",
        "default_result": (
            "0.2 mmol/L — normal (< 0.6 mmol/L). "
            "No significant ketonaemia."
        ),
    },
    "procalcitonin": {
        "label": "Procalcitonin (PCT)",
        "group": "Specialist Bloods & Markers",
        "default_result": (
            "0.05 µg/L — normal (< 0.1 µg/L). "
            "No evidence of significant bacterial infection or sepsis."
        ),
    },
    "b12_folate": {
        "label": "Vitamin B12 & folate",
        "group": "Specialist Bloods & Markers",
        "default_result": (
            "Vitamin B12 420 ng/L (normal 187–900 ng/L). "
            "Folate 9.4 µg/L (normal > 4.0 µg/L) — both normal."
        ),
    },
    "iron_ferritin": {
        "label": "Iron studies & ferritin",
        "group": "Specialist Bloods & Markers",
        "default_result": (
            "Ferritin 72 µg/L (normal). Serum iron 16 µmol/L (normal). "
            "TIBC 58 µmol/L (normal). Transferrin saturation 28% — normal."
        ),
    },
    "haemolysis_screen": {
        "label": "Haemolysis screen (reticulocytes, haptoglobin, blood film)",
        "group": "Specialist Bloods & Markers",
        "default_result": (
            "Reticulocytes 1.2% (normal). Haptoglobin 1.4 g/L (normal). "
            "Blood film: normal red cell morphology. Direct Coombs test negative. "
            "No evidence of haemolysis."
        ),
    },
    "immunoglobulins": {
        "label": "Immunoglobulins & protein electrophoresis",
        "group": "Specialist Bloods & Markers",
        "default_result": (
            "IgG 12.4 g/L · IgA 2.1 g/L · IgM 1.0 g/L — all within normal range. "
            "SPEP: no paraprotein detected."
        ),
    },
    "tumour_markers": {
        "label": "Tumour markers (AFP, CEA, CA-125, CA19-9, PSA)",
        "group": "Specialist Bloods & Markers",
        "default_result": (
            "AFP 3.2 IU/mL (normal) · CEA 1.8 µg/L (normal) · "
            "CA-125 14 U/mL (normal) · CA19-9 12 U/mL (normal) · "
            "PSA < 1.0 µg/L (normal) — no elevated tumour markers."
        ),
    },

    # ── 3. HORMONES, AUTOIMMUNE & METABOLIC ──────────────────────────
    "tsh": {
        "label": "Thyroid function tests (TSH + free T4)",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": (
            "TSH 1.8 mU/L (normal 0.4–4.0 mU/L). "
            "Free T4 16 pmol/L (normal 12–22 pmol/L) — euthyroid."
        ),
    },
    "ft3": {
        "label": "Free T3",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": "Free T3 4.8 pmol/L — normal (3.1–6.8 pmol/L).",
    },
    "anti_tpo": {
        "label": "Anti-TPO antibodies (thyroid peroxidase)",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": "12 IU/mL — negative (reference < 35 IU/mL). No autoimmune thyroid disease.",
    },
    "cortisol": {
        "label": "Morning cortisol / short Synacthen test",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": (
            "09:00 cortisol 420 nmol/L — normal (> 350 nmol/L). "
            "Short Synacthen: peak cortisol 648 nmol/L at 30 min (> 500 = normal). "
            "Adrenal insufficiency excluded."
        ),
    },
    "prolactin": {
        "label": "Prolactin",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": "Prolactin 290 mIU/L — within normal limits (< 600 mIU/L female).",
    },
    "lh_fsh": {
        "label": "LH, FSH, oestradiol / testosterone",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": (
            "LH 5.2 IU/L · FSH 4.8 IU/L — within normal mid-follicular range. "
            "Oestradiol 280 pmol/L (normal). No hormonal abnormality detected."
        ),
    },
    "pth_vit_d": {
        "label": "Parathyroid hormone (PTH) & Vitamin D",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": (
            "Vitamin D 58 nmol/L — sufficient (> 50 nmol/L). "
            "PTH 4.2 pmol/L — normal (1.6–7.5 pmol/L). "
            "No parathyroid or vitamin D abnormality."
        ),
    },
    "vitd": {
        "label": "Vitamin D (25-OH vitamin D)",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": "58 nmol/L — sufficient (> 50 nmol/L). No vitamin D deficiency.",
    },
    "c_peptide": {
        "label": "C-peptide",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": (
            "0.8 nmol/L — within normal limits (0.3–1.3 nmol/L). "
            "Endogenous insulin secretion present — no absolute insulin deficiency."
        ),
    },
    "anti_gad": {
        "label": "Anti-GAD / anti-islet-cell antibodies",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": (
            "Anti-GAD65 < 5 IU/mL — negative. "
            "Anti-islet antibodies negative. "
            "No autoimmune diabetes markers detected."
        ),
    },
    "ana": {
        "label": "ANA screen (antinuclear antibodies)",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": "ANA negative (titre < 1:40). No evidence of systemic autoimmune disease.",
    },
    "anca": {
        "label": "ANCA (anti-neutrophil cytoplasmic antibodies)",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": "ANCA negative (PR3 and MPO both < 2 U/mL). Vasculitis excluded.",
    },
    "rf_anti_ccp": {
        "label": "Rheumatoid factor (RF) & Anti-CCP",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": "RF < 14 IU/mL (negative). Anti-CCP < 7 U/mL (negative). No rheumatoid markers.",
    },
    "complement": {
        "label": "Complement (C3, C4)",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": "C3 1.1 g/L (normal) · C4 0.22 g/L (normal). No complement consumption.",
    },
    "anti_dna": {
        "label": "Anti-dsDNA antibodies",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": "Anti-dsDNA < 10 IU/mL — negative. SLE excluded.",
    },
    "coeliac": {
        "label": "Coeliac screen (anti-tTG IgA + total IgA)",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": (
            "Anti-tTG IgA < 5 U/mL — negative. Total IgA normal (IgA sufficient). "
            "Coeliac disease excluded."
        ),
    },
    "thrombophilia": {
        "label": "Thrombophilia screen",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": (
            "Factor V Leiden: negative. Prothrombin gene mutation: negative. "
            "Protein C: normal. Protein S: normal. Antithrombin: normal. "
            "Antiphospholipid antibodies (DRVVT, anti-cardiolipin, anti-β2GP1): negative. "
            "No inherited thrombophilia identified."
        ),
    },
    "hcg_blood": {
        "label": "Serum βhCG (blood pregnancy test)",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": "βhCG < 2 IU/L — negative. Not pregnant.",
    },
    "hiv_hep": {
        "label": "HIV Ag/Ab + Hepatitis screen (HBsAg, anti-HCV, anti-HAV)",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": (
            "HIV Ag/Ab: non-reactive (negative). "
            "HBsAg: negative. Anti-HCV: negative. Anti-HAV IgM: negative. "
            "No active viral infection detected."
        ),
    },
    "syphilis": {
        "label": "Syphilis serology (VDRL / TPHA)",
        "group": "Hormones, Autoimmune & Metabolic",
        "default_result": "VDRL non-reactive. TPHA negative. No evidence of syphilis.",
    },

    # ── 4. BLOOD GAS & LACTATE ────────────────────────────────────────
    "abg": {
        "label": "Arterial blood gas (ABG) on air",
        "group": "Blood Gas & Lactate",
        "default_result": (
            "pH 7.40 · PaO₂ 12.8 kPa · PaCO₂ 5.0 kPa · HCO₃ 25 mmol/L · "
            "SaO₂ 98% · BE +0.5 — normal. No respiratory or metabolic disturbance."
        ),
    },
    "vbg": {
        "label": "Venous blood gas (VBG)",
        "group": "Blood Gas & Lactate",
        "default_result": (
            "pH 7.38 · pCO₂ 5.4 kPa · HCO₃ 24 mmol/L · BE −0.5 — "
            "no significant acid-base abnormality."
        ),
    },

    # ── 5. MICROBIOLOGY & INFECTION ──────────────────────────────────
    "blood_cultures": {
        "label": "Blood cultures × 2 (peripheral)",
        "group": "Microbiology & Infection",
        "default_result": "No growth after 5 days of incubation — negative for bacteraemia/fungaemia.",
    },
    "urine_culture": {
        "label": "Urine culture & sensitivities (MC&S)",
        "group": "Microbiology & Infection",
        "default_result": (
            "No significant growth (< 10⁴ organisms/mL). "
            "Urinary tract infection excluded."
        ),
    },
    "sputum_culture": {
        "label": "Sputum culture & sensitivities",
        "group": "Microbiology & Infection",
        "default_result": (
            "Normal upper respiratory tract flora. "
            "No pathogenic organisms isolated."
        ),
    },
    "sputum_afb": {
        "label": "Sputum for AFB (TB microscopy × 3)",
        "group": "Microbiology & Infection",
        "default_result": "No acid-fast bacilli seen on microscopy × 3. Mycobacterium tuberculosis not detected.",
    },
    "throat_swab": {
        "label": "Throat swab (bacterial + viral screen)",
        "group": "Microbiology & Infection",
        "default_result": "Negative for Group A Streptococcus and other pathogens. Normal oropharyngeal flora.",
    },
    "stool_culture": {
        "label": "Stool culture & sensitivities",
        "group": "Microbiology & Infection",
        "default_result": (
            "No enteric pathogens isolated (Salmonella, Shigella, Campylobacter, E. coli O157, "
            "Clostridioides difficile toxin — all negative)."
        ),
    },
    "covid_test": {
        "label": "COVID-19 PCR / rapid antigen test",
        "group": "Microbiology & Infection",
        "default_result": "COVID-19 antigen test: negative. COVID-19 PCR: not detected.",
    },
    "monospot": {
        "label": "Monospot / EBV heterophile antibodies",
        "group": "Microbiology & Infection",
        "default_result": "Monospot test: negative. EBV IgM: negative. No evidence of infectious mononucleosis.",
    },
    "malaria_film": {
        "label": "Malaria blood film × 3",
        "group": "Microbiology & Infection",
        "default_result": "No intraerythrocytic parasites detected on thick and thin films × 3. Malaria excluded.",
    },

    # ── 6. URINE TESTS ───────────────────────────────────────────────
    "urinalysis": {
        "label": "Urinalysis (dipstick + microscopy)",
        "group": "Urine Tests",
        "default_result": (
            "Dipstick: protein neg · glucose neg · ketones neg · blood neg · "
            "leucocytes neg · nitrites neg · pH 6.0. "
            "Microscopy: no significant cells or casts. Normal."
        ),
    },
    "urine_preg": {
        "label": "Urine pregnancy test (βhCG)",
        "group": "Urine Tests",
        "default_result": "Urine βhCG: negative. Not pregnant.",
    },
    "urine_pcr": {
        "label": "Urine protein:creatinine ratio (PCR)",
        "group": "Urine Tests",
        "default_result": "Urine PCR 12 mg/mmol — within normal limits (< 15 mg/mmol). No significant proteinuria.",
    },
    "urine_acr": {
        "label": "Urine albumin:creatinine ratio (ACR)",
        "group": "Urine Tests",
        "default_result": "Urine ACR 1.8 mg/mmol — within normal limits (< 3.0 mg/mmol). No microalbuminuria.",
    },
    "urine_osmolality": {
        "label": "Urine osmolality",
        "group": "Urine Tests",
        "default_result": "Urine osmolality 580 mOsmol/kg — concentrated urine, normal.",
    },
    "urine_24h": {
        "label": "24-hour urine collection (protein, creatinine, cortisol)",
        "group": "Urine Tests",
        "default_result": (
            "24h protein < 0.15 g/day (normal). "
            "24h creatinine clearance 92 mL/min (normal). "
            "24h free cortisol 82 nmol/day (normal < 200)."
        ),
    },

    # ── 7. CARDIAC INVESTIGATIONS ────────────────────────────────────
    "ecg": {
        "label": "12-lead ECG",
        "group": "Cardiac Investigations",
        "default_result": (
            "Normal sinus rhythm 72 bpm. Normal axis. "
            "PR interval 160 ms · QRS 88 ms · QTc 418 ms — all normal. "
            "No ST elevation, ST depression, T-wave inversion, Q waves, or bundle branch block."
        ),
    },
    "echo": {
        "label": "Transthoracic echocardiogram (TTE)",
        "group": "Cardiac Investigations",
        "default_result": (
            "Normal LV size and systolic function. EF 62%. "
            "No regional wall motion abnormality. "
            "Normal valvular appearances — no significant stenosis or regurgitation. "
            "Normal RV size and function. No pericardial effusion."
        ),
    },
    "holter": {
        "label": "24-hour ambulatory ECG (Holter monitor)",
        "group": "Cardiac Investigations",
        "default_result": (
            "Sinus rhythm throughout. "
            "No significant arrhythmia, no pauses > 2.5 s, no sustained tachyarrhythmia."
        ),
    },
    "exercise_ecg": {
        "label": "Exercise tolerance test (ETT)",
        "group": "Cardiac Investigations",
        "default_result": (
            "Negative study. Achieved 10 METs. "
            "No chest pain, no ST changes, normal BP and HR response. "
            "No exercise-induced arrhythmia. Good functional capacity."
        ),
    },
    "ctca": {
        "label": "CT coronary angiogram (CTCA / CTCS)",
        "group": "Cardiac Investigations",
        "default_result": (
            "Coronary calcium score 12 (low). "
            "No significant coronary artery stenosis (< 50% in all vessels). "
            "No high-risk plaque features."
        ),
    },
    "coronary_angio": {
        "label": "Invasive coronary angiogram (catheter)",
        "group": "Cardiac Investigations",
        "default_result": (
            "Unobstructed coronary arteries. No angiographically significant stenosis (< 30%). "
            "Normal LVEDP. No coronary artery disease identified."
        ),
    },
    "toe": {
        "label": "Transoesophageal echocardiogram (TOE)",
        "group": "Cardiac Investigations",
        "default_result": (
            "No intracardiac thrombus. "
            "No significant valvular abnormality on detailed assessment. "
            "Normal aortic arch. No PFO or atrial septal defect."
        ),
    },

    # ── 8. IMAGING — X-RAY & CT ──────────────────────────────────────
    "cxr": {
        "label": "Chest X-ray (PA + lateral)",
        "group": "Imaging — X-ray & CT",
        "default_result": (
            "Clear lung fields bilaterally. Normal cardiac silhouette (CTR < 0.5). "
            "No consolidation, pleural effusion, or pneumothorax. "
            "Normal mediastinal contour. No bony abnormality."
        ),
    },
    "axr": {
        "label": "Abdominal X-ray (AXR)",
        "group": "Imaging — X-ray & CT",
        "default_result": (
            "No dilated bowel loops. Normal bowel gas pattern. "
            "No free air under diaphragm. No significant soft tissue mass. "
            "No renal or gallbladder calcification."
        ),
    },
    "ct_head": {
        "label": "CT head (non-contrast)",
        "group": "Imaging — X-ray & CT",
        "default_result": (
            "No intracranial haemorrhage. No acute infarct. No space-occupying lesion. "
            "No significant midline shift. Normal grey-white differentiation. "
            "Age-appropriate sulcal prominence."
        ),
    },
    "ct_chest": {
        "label": "CT thorax (contrast / non-contrast)",
        "group": "Imaging — X-ray & CT",
        "default_result": (
            "No consolidation, no significant lymphadenopathy, no pleural effusion. "
            "No pulmonary nodules or masses. No pericardial collection. Normal."
        ),
    },
    "ctpa": {
        "label": "CT Pulmonary Angiogram (CTPA)",
        "group": "Imaging — X-ray & CT",
        "default_result": (
            "No pulmonary embolism. No filling defects in the pulmonary arteries "
            "to the subsegmental level. Normal pulmonary vasculature. "
            "No right heart strain pattern."
        ),
    },
    "ct_abdomen": {
        "label": "CT abdomen & pelvis (contrast)",
        "group": "Imaging — X-ray & CT",
        "default_result": (
            "Normal solid organ appearances (liver, spleen, pancreas, kidneys, adrenals). "
            "No free fluid or free gas. No lymphadenopathy. Normal bowel configuration. "
            "No acute abnormality."
        ),
    },
    "vq_scan": {
        "label": "V/Q (ventilation-perfusion) scan",
        "group": "Imaging — X-ray & CT",
        "default_result": (
            "Normal ventilation. Normal perfusion. "
            "No perfusion defects. Low probability of pulmonary embolism."
        ),
    },
    "hrct_chest": {
        "label": "HRCT chest (high resolution)",
        "group": "Imaging — X-ray & CT",
        "default_result": (
            "No interstitial lung disease. No bronchiectasis. "
            "No ground-glass opacification or honeycombing. "
            "No emphysema. No parenchymal nodules."
        ),
    },
    "pet_ct": {
        "label": "PET-CT (F-FDG)",
        "group": "Imaging — X-ray & CT",
        "default_result": (
            "No hypermetabolic foci to suggest malignancy. "
            "Normal physiological FDG distribution."
        ),
    },
    "bone_scan": {
        "label": "Bone scan (Tc-99m radionuclide)",
        "group": "Imaging — X-ray & CT",
        "default_result": (
            "No areas of increased tracer uptake. "
            "No evidence of bone metastases or metabolic bone disease."
        ),
    },
    "dexa": {
        "label": "DEXA scan (bone mineral density)",
        "group": "Imaging — X-ray & CT",
        "default_result": (
            "Lumbar spine T-score −0.8. Hip T-score −0.6. "
            "Normal bone mineral density. No osteopaenia or osteoporosis."
        ),
    },
    "mammogram": {
        "label": "Mammogram / breast imaging",
        "group": "Imaging — X-ray & CT",
        "default_result": (
            "No suspicious mass, microcalcification, or asymmetry. "
            "BI-RADS 1 — negative study."
        ),
    },

    # ── 9. IMAGING — MRI & ULTRASOUND ────────────────────────────────
    "mri_brain": {
        "label": "MRI brain (with + without contrast)",
        "group": "Imaging — MRI & Ultrasound",
        "default_result": (
            "No acute infarct, haemorrhage, or space-occupying lesion. "
            "No enhancement to suggest malignancy or infection. "
            "Normal posterior fossa and brainstem. Age-appropriate appearances."
        ),
    },
    "mri_spine": {
        "label": "MRI spine (cervical / thoracic / lumbar)",
        "group": "Imaging — MRI & Ultrasound",
        "default_result": (
            "No cord compression or myelopathy. No disc herniation. "
            "Mild degenerative disc disease (age-appropriate). No cord signal change."
        ),
    },
    "mri_abdomen": {
        "label": "MRI abdomen & pelvis",
        "group": "Imaging — MRI & Ultrasound",
        "default_result": (
            "Normal hepatic, pancreatic, splenic, and renal appearances. "
            "No focal lesions. No significant lymphadenopathy. No ascites."
        ),
    },
    "mri_pituitary": {
        "label": "MRI pituitary (dynamic gadolinium)",
        "group": "Imaging — MRI & Ultrasound",
        "default_result": (
            "Normal pituitary gland size and morphology. "
            "No microadenoma or macroadenoma. Normal stalk and optic chiasm."
        ),
    },
    "mri_cardiac": {
        "label": "Cardiac MRI (CMR)",
        "group": "Imaging — MRI & Ultrasound",
        "default_result": (
            "Normal LV volumes and ejection fraction (EF 62%). "
            "No myocardial oedema or late gadolinium enhancement. "
            "No cardiomyopathy pattern."
        ),
    },
    "uss_abdomen": {
        "label": "Ultrasound abdomen (liver, gallbladder, spleen, pancreas, kidneys)",
        "group": "Imaging — MRI & Ultrasound",
        "default_result": (
            "Normal liver echotexture, no focal lesion. "
            "Gallbladder: no stones, no wall thickening. "
            "Spleen, pancreas, bilateral kidneys — all normal. No free fluid."
        ),
    },
    "uss_thyroid": {
        "label": "USS neck / thyroid ultrasound",
        "group": "Imaging — MRI & Ultrasound",
        "default_result": (
            "Normal thyroid size and homogeneous echotexture. "
            "No nodules. No lymphadenopathy. No vascular abnormality."
        ),
    },
    "uss_renal": {
        "label": "USS renal tract (kidneys, ureters, bladder)",
        "group": "Imaging — MRI & Ultrasound",
        "default_result": (
            "Normal renal size, cortical thickness, and echotexture bilaterally. "
            "No hydronephrosis, no renal masses, no calculi. Normal bladder."
        ),
    },
    "uss_pelvis": {
        "label": "USS pelvis (pelvic USS)",
        "group": "Imaging — MRI & Ultrasound",
        "default_result": (
            "Normal uterine size and echotexture. No fibroids or endometrial thickening. "
            "No adnexal masses. No free fluid in pelvis."
        ),
    },
    "leg_doppler": {
        "label": "Bilateral leg venous Doppler USS",
        "group": "Imaging — MRI & Ultrasound",
        "default_result": (
            "No evidence of deep vein thrombosis bilaterally. "
            "Normal compressibility of femoral, popliteal, and tibial veins. "
            "No intraluminal thrombus."
        ),
    },

    # ── 10. RESPIRATORY & LUNG FUNCTION ──────────────────────────────
    "peak_flow": {
        "label": "Peak expiratory flow rate (PEFR)",
        "group": "Respiratory & Lung Function",
        "default_result": "PEFR 390 L/min — within normal range for height, age, and sex.",
    },
    "spirometry": {
        "label": "Spirometry (FEV₁, FVC, FEV₁/FVC ratio)",
        "group": "Respiratory & Lung Function",
        "default_result": (
            "FEV₁ 3.2 L (98% predicted) · FVC 4.0 L (100% predicted) · "
            "FEV₁/FVC ratio 0.82 — no obstructive or restrictive pattern. Normal spirometry."
        ),
    },
    "dlco": {
        "label": "DLCO / transfer factor (gas transfer)",
        "group": "Respiratory & Lung Function",
        "default_result": "DLCO 92% predicted — normal transfer factor. No diffusion impairment.",
    },
    "bronchoscopy": {
        "label": "Bronchoscopy +/− BAL",
        "group": "Respiratory & Lung Function",
        "default_result": (
            "Normal airway anatomy. No endobronchial lesion or mucus plugging. "
            "BAL differential: normal (macrophages 80%, lymphocytes 12%, neutrophils 7%). "
            "No organisms on culture or microscopy."
        ),
    },
    "pleural_fluid": {
        "label": "Pleural fluid aspiration & analysis",
        "group": "Respiratory & Lung Function",
        "default_result": (
            "No pleural effusion identified on ultrasound prior to aspiration — "
            "procedure not performed."
        ),
    },

    # ── 11. GI PROCEDURES ────────────────────────────────────────────
    "ogd": {
        "label": "OGD / Gastroscopy (upper GI endoscopy)",
        "group": "GI Procedures",
        "default_result": (
            "Normal oesophageal mucosa. Normal gastro-oesophageal junction. "
            "Stomach: normal rugal folds, no ulcer or mass. "
            "D1 and D2: normal duodenal mucosa. No pathology identified."
        ),
    },
    "h_pylori": {
        "label": "H. pylori test (urea breath test / stool antigen)",
        "group": "GI Procedures",
        "default_result": "Urea breath test: negative. H. pylori stool antigen: negative.",
    },
    "colonoscopy": {
        "label": "Colonoscopy (to caecum)",
        "group": "GI Procedures",
        "default_result": (
            "Normal colonic mucosa throughout. Intubation to caecum confirmed. "
            "No polyps, no malignancy, no inflammation. Normal ileocaecal valve and terminal ileum."
        ),
    },
    "flexible_sig": {
        "label": "Flexible sigmoidoscopy",
        "group": "GI Procedures",
        "default_result": "Normal sigmoid and descending colon mucosa to the splenic flexure. No lesions identified.",
    },
    "calprotectin": {
        "label": "Faecal calprotectin",
        "group": "GI Procedures",
        "default_result": (
            "42 µg/g — normal (< 50 µg/g). "
            "No evidence of intestinal inflammation. IBD less likely."
        ),
    },
    "fit": {
        "label": "Faecal immunochemical test (FIT)",
        "group": "GI Procedures",
        "default_result": "FIT: negative. No occult blood detected.",
    },
    "ercp": {
        "label": "ERCP (endoscopic retrograde cholangiopancreatography)",
        "group": "GI Procedures",
        "default_result": "Normal biliary and pancreatic duct anatomy. No filling defects or strictures.",
    },
    "capsule_endoscopy": {
        "label": "Capsule endoscopy (small bowel)",
        "group": "GI Procedures",
        "default_result": "Normal small bowel mucosa throughout. No active bleeding, no mass, no stricture.",
    },

    # ── 12. NEUROLOGY ────────────────────────────────────────────────
    "lumbar_puncture": {
        "label": "Lumbar puncture (CSF analysis)",
        "group": "Neurology",
        "default_result": (
            "Opening pressure 14 cmH₂O (normal). CSF appearance: clear and colourless. "
            "Protein 0.34 g/L (normal < 0.45). Glucose 3.8 mmol/L (normal; serum glucose 5.4). "
            "White cells: 1/µL (normal < 5). Red cells: 0. No xanthochromia. "
            "Gram stain: no organisms. Culture: no growth. Viral PCR: negative."
        ),
    },
    "eeg": {
        "label": "EEG (electroencephalogram)",
        "group": "Neurology",
        "default_result": (
            "Normal background alpha rhythm. No epileptiform discharges. "
            "No focal slowing or generalised abnormality."
        ),
    },
    "emg_ncs": {
        "label": "EMG + nerve conduction studies",
        "group": "Neurology",
        "default_result": (
            "Normal motor and sensory nerve conduction velocities and amplitudes. "
            "No evidence of neuropathy, myopathy, or neuromuscular junction disease."
        ),
    },

    # ── 13. CLINICAL DECISION TOOLS ──────────────────────────────────
    "wells_score": {
        "label": "Wells PE Score (clinical calculation)",
        "group": "Clinical Decision Tools",
        "default_result": (
            "To calculate Wells PE Score, consider: "
            "Clinical signs of DVT (+3) · PE most likely diagnosis (+3) · "
            "HR > 100 (+1.5) · Immobilisation / surgery in past 4 weeks (+1.5) · "
            "Previous DVT/PE (+1.5) · Haemoptysis (+1) · Malignancy (+1). "
            "Score ≥ 5 = high probability (proceed to CTPA). "
            "Score 2-4 = moderate (D-dimer then consider CTPA). "
            "Score < 2 = low (D-dimer to exclude)."
        ),
    },
    "wells_dvt": {
        "label": "Wells DVT Score (clinical calculation)",
        "group": "Clinical Decision Tools",
        "default_result": (
            "To calculate Wells DVT Score, consider: "
            "Active cancer (+1) · Paralysis / immobility (+1) · Bedridden ≥ 3 days or surgery ≤ 12 weeks (+1) · "
            "Localised tenderness (+1) · Entire leg swollen (+1) · Calf swelling > 3 cm (+1) · "
            "Pitting oedema (+1) · Collateral superficial veins (+1) · Previous DVT (+1) · "
            "Alternative diagnosis as likely or more likely (−2). "
            "Score ≥ 2 = moderate-high probability (USS)."
        ),
    },
    "curb65": {
        "label": "CURB-65 score (community-acquired pneumonia severity)",
        "group": "Clinical Decision Tools",
        "default_result": (
            "CURB-65 components: Confusion (new, AMT ≤ 8) · Urea > 7 mmol/L · "
            "Respiratory rate ≥ 30/min · BP systolic < 90 or diastolic ≤ 60 mmHg · "
            "Age ≥ 65 years. "
            "Score 0-1 = low severity (outpatient treatment). "
            "Score 2 = moderate (hospital admission). "
            "Score ≥ 3 = severe (HDU/ICU consideration)."
        ),
    },
    "amts": {
        "label": "Abbreviated Mental Test Score (AMTS) / 4AT delirium screen",
        "group": "Clinical Decision Tools",
        "default_result": (
            "4AT delirium screening tool: "
            "[A] Alertness · [4] AMT4 (age, DOB, place, year) · "
            "[T] Attention (months backwards) · [T] Acute change / fluctuating course. "
            "Score 0 = unlikely delirium. Score 1-3 = possible delirium. Score ≥ 4 = likely delirium. "
            "Requires clinical assessment to complete."
        ),
    },
}


# ── Group ordering ────────────────────────────────────────────────────
# Controls the order collapsible groups appear in the UI.
# Maps group name → list of keys in display order.

INV_GROUPS = {
    "🩸 Routine Bloods": [
        "fbc", "ue", "lft", "amylase", "lipase", "lipids",
        "glucose", "hba1c", "crp", "esr", "coag", "bone_profile", "urate",
        "ck", "ldh",
    ],
    "🔬 Specialist Bloods & Markers": [
        "troponin", "bnp", "d_dimer", "lactate", "blood_ketones",
        "procalcitonin", "b12_folate", "iron_ferritin", "haemolysis_screen",
        "immunoglobulins", "tumour_markers",
    ],
    "⚗️ Hormones, Autoimmune & Metabolic": [
        "tsh", "ft3", "anti_tpo", "cortisol", "prolactin", "lh_fsh",
        "pth_vit_d", "c_peptide", "anti_gad", "coeliac", "thrombophilia",
        "ana", "anca", "rf_anti_ccp", "complement", "anti_dna",
        "hcg_blood", "hiv_hep", "syphilis",
    ],
    "💨 Blood Gas & Lactate": [
        "abg", "vbg",
    ],
    "🦠 Microbiology & Infection": [
        "blood_cultures", "urine_culture", "sputum_culture", "sputum_afb",
        "throat_swab", "stool_culture", "covid_test", "monospot", "malaria_film",
    ],
    "💧 Urine Tests": [
        "urinalysis", "urine_preg", "urine_pcr", "urine_acr",
        "urine_osmolality", "urine_24h",
    ],
    "❤️ Cardiac Investigations": [
        "ecg", "echo", "holter", "exercise_ecg", "ctca", "coronary_angio", "toe",
    ],
    "📷 Imaging — X-ray & CT": [
        "cxr", "axr", "ct_head", "ct_chest", "ctpa", "ct_abdomen",
        "hrct_chest", "vq_scan", "pet_ct", "bone_scan", "dexa", "mammogram",
    ],
    "🔭 Imaging — MRI & Ultrasound": [
        "mri_brain", "mri_spine", "mri_abdomen", "mri_pituitary", "mri_cardiac",
        "uss_abdomen", "uss_thyroid", "uss_renal", "uss_pelvis", "leg_doppler",
    ],
    "🫁 Respiratory & Lung Function": [
        "peak_flow", "spirometry", "dlco", "bronchoscopy", "pleural_fluid",
    ],
    "🔬 GI Procedures": [
        "ogd", "h_pylori", "colonoscopy", "flexible_sig",
        "calprotectin", "fit", "ercp", "capsule_endoscopy",
    ],
    "🧠 Neurology": [
        "lumbar_puncture", "eeg", "emg_ncs",
    ],
    "📊 Clinical Decision Tools": [
        "wells_score", "wells_dvt", "curb65", "amts",
    ],
}
