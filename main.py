from nlp_engine import extract_info, analyze_resume

def main():
    print("🔍 Analyzing resume...\n")
    with open("sample_resume.txt", "r", encoding="utf-8") as file:
        resume_text = file.read()

    info = extract_info(resume_text)
    feedback = analyze_resume(info)

    print("🧠 Detected Skills:")
    for skill in info['skills']:
        print(f"- {skill}")

    print("\n🎓 Education:")
    print(info.get('education', 'Not Found'))

    print("\n📢 Feedback:")
    for item in feedback:
        print(item)

if __name__ == "__main__":
    main()
