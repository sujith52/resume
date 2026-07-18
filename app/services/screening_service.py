from pathlib import Path

from app.extractor.extractor import extract_resume_data
from app.parser.jd_loader import load_job_description
from app.parser.resume_parser import extract_text
from app.scorer.scorer import calculate_similarity

from app.scorer.ranker import rank_candidates


def screen_all_resumes(
    resume_folder: Path,
    jd_path: Path
):
    """
    Process all resumes and generate candidate scores.
    """

    job_description = load_job_description(jd_path)

    candidates = []

    for resume in resume_folder.iterdir():

        if resume.suffix.lower() not in [
            ".pdf",
            ".docx",
            ".txt"
        ]:
            continue

        print(f"Processing {resume.name}...")

        resume_text = extract_text(resume)

        resume_data = extract_resume_data(
            resume_text, resume.stem
        )

        similarity = calculate_similarity(
            job_description,
            resume_text
        )

        resume_data["score"] = round(
            similarity * 100,
            2
        )

        candidates.append(resume_data)

    return rank_candidates(candidates)