# components/summarizer.py

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

LLM_MODEL = "gpt-4o"  # or gpt-3.5-turbo if needed

def generate_summary(chunks, max_words=1000) -> str:
    combined = " ".join(chunks)[:4000]  # Basic input limit control

    system_prompt = (
        "You are a helpful research assistant. Your task is to write an executive summary of the following document. "
        "Focus on key findings, ideas, or arguments. Be concise and informative."
    )

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": combined}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()


def suggest_reading(chunks, max_topics=5) -> list:
    combined = " ".join(chunks)[:4000]

    system_prompt = (
        "Based on the document, suggest a few (3–5) follow-up reading topics. "
        "These should be specific areas or terms the reader might want to learn more about."
    )

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": combined}
        ],
        temperature=0.4
    )

    raw_output = response.choices[0].message.content.strip()

    return [line.strip("-• ") for line in raw_output.splitlines() if line.strip()]
