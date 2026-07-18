from pathlib import Path

import pdfplumber
from docx import Document

# pdf files 
def read_pdf(file_path: Path) -> str:
    """
    Extract text from a PDF file.
    """

    text = []

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text.append(page_text)

        return "\n".join(text)

    except Exception as e:
        print(f"Error reading PDF {file_path}: {e}")
        return ""


# doc function 

def read_docx(file_path: Path) -> str:
    """
    Extract text from a DOCX file.
    """

    try:
        document = Document(file_path)

        paragraphs = []

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                paragraphs.append(paragraph.text)

        return "\n".join(paragraphs)

    except Exception as e:
        print(f"Error reading DOCX {file_path}: {e}")
        return ""

# txt files 

def read_txt(file_path: Path) -> str:
    """
    Extract text from a TXT file.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except Exception as e:
        print(f"Error reading TXT {file_path}: {e}")
        return ""


def extract_text(file_path: Path) -> str:
    """
    Extract text from PDF, DOCX, or TXT files.
    """

    suffix = file_path.suffix.lower()

    if suffix == ".pdf":
        return read_pdf(file_path)

    elif suffix == ".docx":
        return read_docx(file_path)

    elif suffix == ".txt":
        return read_txt(file_path)

    else:
        raise ValueError(f"Unsupported file format: {suffix}")