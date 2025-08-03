import json
import os
import httpx
from tool_registry import tool_registry
from memory.memory_store import MemoryStore
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY not set in environment variables")

base_url = "https://openrouter.ai/api/v1"
headers = {
    "Authorization": f"Bearer {api_key}",
    "HTTP-Referer": "https://yourdomain.com",
    "X-Title": "Your App"
}

memory = MemoryStore("memory/conversation.json")

MODEL = "z-ai/glm-4.5-air:free"

def detect_tool_call(user_input):
    for name in tool_registry:
        if name in user_input.lower():
            return name
    return None

def build_prompt(user_input):
    history = memory.get_memory()
    messages = history + [
        {"role": "user", "content": user_input}
    ]
    return messages

def run_agent(user_input):
    tool_name = detect_tool_call(user_input)

    if tool_name:
        tool_func = tool_registry[tool_name]
        result = tool_func(user_input)
        memory.add_exchange("user", user_input)
        memory.add_exchange("assistant", result)
        return f"Using tool `{tool_name}`: {result}"

    messages = build_prompt(user_input)
    try:
        response = httpx.post(
            f"{base_url}/chat/completions",
            headers=headers,
            json={
                "model": MODEL,
                "messages": messages
            },
            timeout=30
        )
        response.raise_for_status()
        reply = response.json()["choices"][0]["message"]["content"]
        memory.add_exchange("user", user_input)
        memory.add_exchange("assistant", reply)
        return reply
    except Exception as e:
        return f"Error: {e}"