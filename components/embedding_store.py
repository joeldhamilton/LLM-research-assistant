# components/embedding_store.py

import faiss
import numpy as np
from typing import List
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Global variables
index = None
chunk_lookup = []

EMBEDDING_MODEL = "text-embedding-3-small"

def get_embedding(text: str) -> List[float]:
    """Returns the embedding vector for a given text using the new OpenAI API."""
    response = client.embeddings.create(
        input=[text],
        model=EMBEDDING_MODEL
    )
    return response.data[0].embedding


def create_vector_store(chunks: List[str]):
    """Creates a FAISS index and stores chunk embeddings."""
    global index, chunk_lookup

    chunk_lookup = chunks

    embeddings = [get_embedding(chunk) for chunk in chunks]
    vectors = np.array(embeddings).astype('float32')

    dim = vectors.shape[1]
    index_flat = faiss.IndexFlatL2(dim)
    index_flat.add(vectors)

    index = index_flat


def search_similar_chunks(query: str, k: int = 3) -> List[str]:
    """Searches the FAISS index for top-k most similar chunks."""
    global index, chunk_lookup

    if index is None:
        raise ValueError("FAISS index not initialized. Did you call create_vector_store()?")

    query_embedding = np.array([get_embedding(query)]).astype('float32')
    distances, indices = index.search(query_embedding, k)

    return [chunk_lookup[i] for i in indices[0]]
