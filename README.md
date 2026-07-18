# AI Resume Screening Agent

An AI-powered Resume Screening Agent built with **FastAPI**, **Google Gemini**, and **Scikit-learn** that automatically ranks resumes against a given Job Description (JD).

The application parses resumes in **PDF**, **DOCX**, and **TXT** formats, extracts structured candidate information using the **Google Gemini API**, computes resume relevance using **TF-IDF + Cosine Similarity**, ranks candidates, and exports the results as **JSON** and **CSV**.

This project was developed as a submission for the **ROOMAN AI – 24 Hour AI Agent Challenge**.
# AI Resume Screening Agent

## 🎥 Project Demo

https://github.com/user-attachments/assets/a0b3687c-5e7a-4213-a189-7965799640c5
## Features

* Parse resumes from PDF, DOCX, and TXT files
* Load a Job Description (JD)
* Extract candidate information using Google Gemini

  * Candidate Name
  * Skills
  * Experience
  * Education
* Calculate resume relevance using TF-IDF and Cosine Similarity
* Rank candidates based on relevance score
* Export ranked candidates to JSON and CSV
* FastAPI REST API
* Interactive Swagger Documentation
* Local caching to reduce repeated Gemini API calls

---

## Tech Stack

### Backend

* Python 3.12
* FastAPI

### AI

* Google Gemini API

### NLP

* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity

### File Processing

* pdfplumber
* python-docx

### Utilities

* python-dotenv
* JSON
* CSV

---
## Project Structure

```text
resume/
│
├── app/
│   ├── api/
│   │   └── routes.py                 # FastAPI API endpoints
│   │
│   ├── extractor/
│   │   └── extractor.py              # Gemini-based resume information extraction
│   │
│   ├── parser/
│   │   ├── jd_loader.py              # Loads the Job Description
│   │   └── resume_parser.py          # Parses PDF, DOCX, and TXT resumes
│   │
│   ├── scorer/
│   │   ├── scorer.py                 # TF-IDF & Cosine Similarity scoring
│   │   └── ranker.py                 # Sorts candidates by score
│   │
│   ├── schemas/
│   │   └── request.py                # FastAPI request models
│   │
│   ├── services/
│   │   └── screening_service.py      # Orchestrates the complete screening pipeline
│   │
│   └── utils/
│       ├── cache.py                  # Caches Gemini responses
│       └── helpers.py                # Common helper functions
│
├── data/
│   ├── resumes/                      # Sample resumes
│   ├── outputs/                      # Generated CSV and JSON results
│   ├── cache/                        # Cached Gemini extraction results
│   └── jd.txt                        # Sample Job Description
│
├── main.py                           # FastAPI application entry point
├── requirements.txt                  # Python dependencies
├── README.md                         # Project documentation
└── .env                              # Gemini API key (not committed)
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sujith52/resume.git
cd ai-resume-analyzer
```

### 2. Create a Virtual Environment

**Linux / macOS / GitHub Codespaces**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a file named `.env` in the project root.

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Prepare Input Data

Place your resumes inside:

```text
data/resumes/
```

Place your Job Description at:

```text
data/jd.txt
```

### 6. Start the FastAPI Server

```bash
uvicorn main:app --reload
```

If the server starts successfully, you should see output similar to:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### 7. Open the API Documentation

Open your browser and visit:

```text
http://127.0.0.1:8000/docs
```

FastAPI provides an interactive Swagger UI where you can test the API directly.

---

## API Usage

### Endpoint

```http id="fhb7j8"
POST /screen
```

### Request Body

```json id="79tr7k"
{
    "resume_folder": "data/resumes",
    "jd_path": "data/jd.txt"
}
```

### Successful Response

```json id="0qg5cq"
{
    "total_candidates": 5,
    "results": [
        {
            "name": "Sujith Kumar Gavathakatla",
            "skills": [
                "Python",
                "FastAPI",
                "React",
                "SQL"
            ],
            "experience_years": 0.33,
            "education": "Bachelor of Technology in Computer Science and Engineering",
            "score": 16.93
        }
    ]
}
```

### Generated Output Files

After a successful screening process, the application automatically generates:

```text id="9l7crl"
data/outputs/
├── ranked_candidates.json
└── ranked_candidates.csv
```

The JSON file contains structured candidate information, while the CSV file provides a recruiter-friendly ranked list that can be opened in spreadsheet applications.

---
## Scoring Method

The Resume Screening Agent uses a hybrid approach that combines **AI-based information extraction** with **traditional NLP similarity scoring**.

### Step 1 — Resume Parsing

The application first reads resumes in **PDF**, **DOCX**, and **TXT** formats and converts them into plain text.

### Step 2 — AI-Based Information Extraction

Each parsed resume is sent to the **Google Gemini API**, which extracts structured candidate information, including:

* Candidate Name
* Technical Skills
* Years of Experience
* Education

To reduce API usage and improve performance, extracted results are cached locally. If the same resume is processed again without changes, the cached result is used instead of making another Gemini API request.

### Step 3 — Job Description Loading

The Job Description (JD) is loaded from a text file and used as the reference document for comparison.

### Step 4 — NLP Similarity Calculation

The resume text and the Job Description are converted into numerical vectors using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

The similarity between these vectors is then calculated using **Cosine Similarity**, producing a relevance score that indicates how closely a resume matches the Job Description.

### Step 5 — Candidate Ranking

Each candidate receives a final relevance score based on the TF-IDF and Cosine Similarity calculation.

Candidates are sorted in descending order of their scores, producing a ranked shortlist from the most relevant to the least relevant candidate.

### Why This Approach?

This project combines the strengths of two techniques:

* **Google Gemini** extracts structured information from resumes with different formats and layouts.
* **TF-IDF + Cosine Similarity** provides a fast, lightweight, and explainable method for comparing resume content with the Job Description.

This hybrid approach is simple, reproducible, and computationally efficient, making it suitable for screening multiple resumes in a single run.

---
## Sample Input & Output

### Sample Job Description

```text
Looking for a Backend Python Developer with experience in Python, FastAPI,
REST APIs, SQL, PostgreSQL, Git, and Machine Learning fundamentals.
```

### Sample Resume

```text
Name: Sujith Kumar Gavathakatla

Skills:
Python, FastAPI, React, SQL, PostgreSQL,
Git, NumPy, Pandas, Scikit-learn

Education:
Bachelor of Technology in Computer Science and Engineering

Experience:
Backend Python Intern
```

### Sample Output

```json
{
    "name": "Sujith Kumar Gavathakatla",
    "experience_years": 0.33,
    "education": "Bachelor of Technology in Computer Science and Engineering",
    "score": 16.93
}
```

The application also generates:

```text
data/outputs/
├── ranked_candidates.csv
└── ranked_candidates.json
```

These files contain the ranked list of all processed candidates along with their relevance scores.

---
## Tradeoffs & Future Improvements

### Design Decisions

This project was designed with the goal of building a complete, working AI Resume Screening Agent within a limited development timeframe. The focus was on creating a modular, maintainable, and easily reproducible solution.

### Tradeoffs

#### Why Google Gemini?

Google Gemini was used to extract structured information from resumes because resumes often have inconsistent layouts and formatting. Using an LLM makes it easier to identify candidate details such as skills, education, and experience without writing complex parsing rules.

#### Why TF-IDF + Cosine Similarity?

TF-IDF combined with Cosine Similarity provides a lightweight, explainable, and efficient NLP approach for measuring how closely a resume matches a Job Description.

While embedding-based models generally provide better semantic understanding, TF-IDF is computationally inexpensive, requires no additional infrastructure, and is well suited for processing multiple resumes quickly.

#### Caching

Gemini responses are cached locally to avoid repeated API calls for the same resume. This reduces API usage, improves response time, and prevents unnecessary consumption of request quotas.

### Current Limitations

* Scanned or image-only PDF resumes are not supported because text extraction requires selectable text.
* Candidate ranking currently relies on textual similarity and does not evaluate the quality or impact of experience.
* Skill matching is based on extracted text and does not consider synonyms or related technologies.
* The API currently expects local file paths rather than direct file uploads.

### Future Improvements

* Replace TF-IDF with embedding-based semantic search for improved matching accuracy.
* Add resume and Job Description file upload support through the API.
* Store screening history in a database.
* Generate detailed explanations showing matched and missing skills for each candidate.
* Containerize the application using Docker.
* Deploy the application to a cloud platform such as Render, Railway, or Azure.
* Build a React-based frontend for recruiters to upload resumes and visualize rankings.

---

## License

This project was developed for the **ROOMAN AI – 24 Hour AI Agent Challenge** as part of the Junior AI Research Associate selection process.

The project is intended for educational and demonstration purposes.
## Note

The sample resumes included during development were sourced from publicly available resume examples and belong to their respective owners.

They are included solely for demonstrating and testing the end-to-end workflow of the Resume Screening Agent, including parsing, information extraction, similarity scoring, and candidate ranking. No ownership of these resumes is claimed.

If you are one of the original authors and would like your resume removed from this repository, please open an issue or contact me, and I will remove it promptly.
