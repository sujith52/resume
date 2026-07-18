from pathlib import Path

from app.parser.resume_parser import extract_text
from app.parser.jd_loader import load_job_description
from app.scorer.scorer import calculate_similarity

resume_path = Path("data/resumes/resume.pdf")
jd_path = Path("data/jd.txt")

resume_text = extract_text(resume_path)
jd_text = load_job_description(jd_path)


score = calculate_similarity(jd_text, resume_text)

print("=" * 50)
print("Resume Screening Result")
print("=" * 50)

print(f"Similarity Score: {score:.2f}")

print("=" * 50)