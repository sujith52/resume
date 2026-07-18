import json
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def extract_resume_data(resume_text: str) -> dict:
    """
    Extract structured information from a resume using Gemini.
    """

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
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()
    
    if text.startswith("```json"):
        text = text.replace("```json", "", 1)

    if text.endswith("```"):
        text = text[:-3]

    text = text.strip()

    return json.loads(text)