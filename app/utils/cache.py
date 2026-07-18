import json
from pathlib import Path


CACHE_DIR = Path("data/cache")


def get_cache_path(resume_name: str):
    """
    Return cache file path for a resume.
    """

    CACHE_DIR.mkdir(
        exist_ok=True
    )

    return CACHE_DIR / f"{resume_name}.json"



def save_cache(resume_name: str, data: dict):
    """
    Save extracted resume data.
    """

    cache_file = get_cache_path(resume_name)

    with open(
        cache_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )



def load_cache(resume_name: str):
    """
    Load cached resume data if available.
    """

    cache_file = get_cache_path(resume_name)


    if cache_file.exists():

        with open(
            cache_file,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    return None