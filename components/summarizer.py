# components/summarizer.py

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

LLM_MODEL = "gpt-4o"  # Use gpt-3.5-turbo if needed

def generate_summary(chunks, max_words=1000) -> str:
    """Creates an executive summary from the full document chunks."""
    combined = " ".join(chunks)[:4000]  # Keep input within LLM token limits

    system_prompt = (
        "You are a helpful research assistant. Your task is to write an executive summary of the following document. "
        "Focus on key findings, ideas, or arguments. Be concise and informative."
    )

    response = openai.ChatCompletion.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": combined}
        ],
        temperature=0.3
    )

    return response["choices"][0]["message"]["content"].strip()


def suggest_reading(chunks, max_topics=5) -> list:
    """Suggests follow-up reading topics or terms based on document content."""
    combined = " ".join(chunks)[:4000]

    system_prompt = (
        "Based on the document, suggest a few (3–5) follow-up reading topics. "
        "These should be specific areas or terms the reader might want to learn more about."
    )

    response = openai.ChatCompletion.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": combined}
        ],
        temperature=0.4
    )

    raw_output = response["choices"][0]["message"]["content"].strip()

    # Split into a clean list
    return [line.strip("-• ") for line in raw_output.splitlines() if line.strip()]
