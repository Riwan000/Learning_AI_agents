import os
import requests
from dotenv import load_dotenv
from config import SYSTEM_PROMPT

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "z-ai/glm-4.5-air:free"  # or change to any supported model

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",  # Customize this
    "X-Title": "ModularAgent-Day3"
}

class ModularAgent:
    def __init__(self, system_prompt=SYSTEM_PROMPT):
        self.messages = [{"role": "system", "content": system_prompt}]

    def chat(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        payload = {
            "model": MODEL,
            "messages": self.messages
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        result = response.json()

        reply = result["choices"][0]["message"]["content"]
        self.messages.append({"role": "assistant", "content": reply})
        return reply
