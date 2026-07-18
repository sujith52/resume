from pathlib import Path


def load_job_description(file_path: Path) -> str:
    """
    Load the Job Description from a text file.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except Exception as e:
        print(f"Error loading Job Description: {e}")
        return ""