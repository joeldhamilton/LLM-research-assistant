# components/document_loader.py

import fitz  # PyMuPDF
from newspaper import Article
import tempfile

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
    """Extracts text from a web page using newspaper3k."""
    article = Article(url)
    article.download()
    article.parse()
    return article.text.strip()
