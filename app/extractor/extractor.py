import json
import os

from dotenv import load_dotenv
from google import genai

from app.utils.cache import save_cache, load_cache


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_resume_data(resume_text: str, resume_name: str) -> dict:
    """
    Extract structured information from a resume using Gemini.
    Uses cache to avoid repeated API calls.
    """

    # 1. Check cache first
    cached_data = load_cache(resume_name)

    if cached_data:
        print(f"Using cache for {resume_name}")
        return cached_data


    # 2. If cache doesn't exist, call Gemini
    print(f"Calling Gemini for {resume_name}")


    prompt = f"""
You are an expert ATS resume parser.

Extract the following information from the resume.

Return ONLY valid JSON.

{{
    "name": "",
    "skills": [],
    "experience_years": 0,
    "education": ""
}}

Resume:

{resume_text}
"""


    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )


    text = response.text.strip()


    if text.startswith("```json"):
        text = text.replace("```json", "", 1)


    if text.endswith("```"):
        text = text[:-3]


    text = text.strip()


    resume_data = json.loads(text)


    # 3. Save Gemini result into cache
    save_cache(
        resume_name,
        resume_data
    )


    return resume_data