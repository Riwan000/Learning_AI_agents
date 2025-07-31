"""
An AI agent is a purposeful, persistent, 
and responsive system that acts based on 
input, holds context, and has a role or goal.
"""

import os
import requests
from dotenv import load_dotenv
from agent_config import SYSTEM_PROMPT

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

# ✅ Correct model and API endpoint
MODEL = "qwen/qwen3-30b-a3b-instruct-2507"  # Free model supported on OpenRouter
API_URL = "https://openrouter.ai/api/v1/chat/completions"  
print(API_KEY)

# ✅ Required headers for OpenRouter
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",  # Customize this for deployment
    "X-Title": "Day1-Agent"
}

# Start conversation with system prompt
messages = [{"role": "system", "content": SYSTEM_PROMPT}]

print("Agent is ready. Type 'exit' to quit.\n")

while True:
    user_input = input("You : ")
    if user_input.lower() in ['exit', 'quit']:
        break

    messages.append({"role": "user", "content": user_input})

    data = {
        "model": MODEL,
        "messages": messages
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()

        res_json = response.json()

        if "choices" in res_json:
            reply = res_json["choices"][0]["message"]["content"]
            print(f"Agent: {reply}\n")
            messages.append({"role": "assistant", "content": reply})
        else:
            print("Unexpected response format:\n", res_json)

    except Exception as e:
        print("Error:", e)
        print("Raw response:\n", response.text)
