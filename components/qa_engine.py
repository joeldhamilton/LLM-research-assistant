# components/qa_engine.py

from openai import OpenAI
import os
from dotenv import load_dotenv
from components.embedding_store import search_similar_chunks

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

LLM_MODEL = "gpt-4o"  # You can switch to gpt-3.5-turbo if preferred

def answer_question(question: str, k: int = 3) -> str:
    """Answers a question based on top-k retrieved document chunks."""
    context_chunks = search_similar_chunks(question, k=k)
    context = "\n\n".join(context_chunks)

    system_prompt = (
        "You are an expert research assistant. Answer questions using the context provided. "
        "Be concise, accurate, and grounded in the document. If the answer is not found in the context, say you don't know."
    )

    user_prompt = f"""Context:\n{context}\n\nQuestion: {question}"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()
