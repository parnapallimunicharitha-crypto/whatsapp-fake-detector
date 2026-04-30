from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate_to_english(text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": f"Translate to English:\n{text}"}]
    )
    return response.choices[0].message.content


def translate_to_telugu(text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": f"Translate to Telugu:\n{text}"}]
    )
    return response.choices[0].message.content


# ✅ ADD THIS (fix your error)
def translate_to_original(text, lang):
    if lang == "te":
        return translate_to_telugu(text)
    return text