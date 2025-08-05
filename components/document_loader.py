# components/document_loader.py

import fitz  # PyMuPDF
import tempfile
import requests
from bs4 import BeautifulSoup

def load_pdf(uploaded_file):
    """Extracts text from an uploaded PDF file."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    doc = fitz.open(tmp_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text.strip()


def load_url(url):
    """Extracts text from a web page using BeautifulSoup (Streamlit-compatible)."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Remove unwanted tags
    for tag in soup(["script", "style", "noscript", "footer", "header", "form", "svg", "aside"]):
        tag.decompose()

    # Extract readable paragraph text
    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
    text = "\n".join(paragraphs)

    return text.strip()
