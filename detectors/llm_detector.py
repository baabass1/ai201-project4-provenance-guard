from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def detect_ai(text):
    prompt = f"""
Determine whether the following text was likely written by an AI or a human.

Respond with ONLY one number between 0 and 100.
0 means definitely human.
100 means definitely AI.

Text:
{text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    score = response.choices[0].message.content.strip()

    return int(score)