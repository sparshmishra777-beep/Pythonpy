# ******* RESUME ANALYZER PROJECT ******* #


file = open("resume.txt","r")
resume_text = file.read().lower()
file.close()

skills_input = input("Enter required job skills (comma separated):")
job_skills = skills_input.lower().split(",")

clean_job_skills = []
for skill in job_skills:
    clean_job_skills.append(skill.strip())

matched = []
missing = []

for skill in clean_job_skills :
    if skill in resume_text:
        matched.append(skill)

    else:
        missing.append(skill)

match_percentage = (len(matched)/len(clean_job_skills)) * 100

print("\n📊 Resume Analysis Result")
print("Match Percentage:",round(match_percentage, 2), "%")

print("\n✅ Matched Skills:")
for skill in matched:
    print("-",skill)

print("\n❌ Missing Skills:")
for skill in missing:
    print("-",skill)