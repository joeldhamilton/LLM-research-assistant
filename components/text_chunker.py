# components/text_chunker.py

import re
from typing import List

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """
    Splits a long string into overlapping chunks of approximately `chunk_size` words.
    Uses simple whitespace tokenization for now.
    """
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))

    return chunks
