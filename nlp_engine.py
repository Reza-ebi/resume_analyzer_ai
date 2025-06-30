import spacy
import re
import json

# Load English model
nlp = spacy.load("en_core_web_sm")

# Load skills from JSON
with open("skill_database.json", "r") as f:
    SKILLS = set(json.load(f)["skills"])

def extract_info(text):
    doc = nlp(text)
    skills_found = set()
    education = ""

    # Find skill words
    for token in doc:
        word = token.text.lower()
        if word in SKILLS:
            skills_found.add(word)

    # Find education
    education_match = re.search(r"(bsc|msc|phd|bachelor|master).*?in.*?(\\n|\\.)", text, re.IGNORECASE)
    if education_match:
        education = education_match.group().strip()

    return {
        "skills": sorted(list(skills_found)),
        "education": education
    }

def analyze_resume(info):
    feedback = []
    skills = info['skills']

    # Strengths
    if "cloud" in skills:
        feedback.append("✅ Strong experience in cloud technologies.")
    if "python" in skills:
        feedback.append("✅ Proficient in Python programming.")
    if "nlp" in skills:
        feedback.append("✅ Familiarity with Natural Language Processing.")

    # Suggestions
    if "teaching" not in skills:
        feedback.append("⚠️ No mention of teaching experience found.")
    if "github" not in skills:
        feedback.append("💡 Consider adding your GitHub or open-source projects.")
    if not info.get("education"):
        feedback.append("⚠️ Education details not clearly found.")

    return feedback
