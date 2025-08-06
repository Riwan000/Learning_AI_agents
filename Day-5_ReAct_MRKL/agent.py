import json
import os
import requests
from tools.search_tool import web_search
from tools.math_tool import calculator
from prompts import system_prompt, tool_prompt_template, final_prompt_template
from memory import trim_messages
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "mistralai/mistral-7b-instruct"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://your-site.com",  # Optional but recommended
    "X-Title": "Your App Name"               # Optional
}

def call_model(messages, functions=None):
    body = {
        "model": MODEL,
        "messages": messages,
    }

    if functions:
        body["functions"] = functions

    response = requests.post(API_URL, headers=HEADERS, json=body)

    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

    data = response.json()
    return data["choices"][0]["message"]

def run_agent(user_input, memory):
    memory.append({"role": "user", "content": user_input})
    memory = trim_messages(memory)

    tools = {
        "calculator": calculator,
        "web_search": web_search
    }

    # First call to determine if a tool should be used
    response = call_model(memory)

    if response.get("function_call"):
        name = response["function_call"]["name"]
        args = json.loads(response["function_call"]["arguments"])
        tool_func = tools.get(name)

        if tool_func:
            result = tool_func(**args)
            memory.append({"role": "assistant", "content": None, "function_call": response["function_call"]})
            memory.append({"role": "function", "name": name, "content": result})

            final_response = call_model(memory)
            memory.append({"role": "assistant", "content": final_response["content"]})
            return final_response["content"], memory
        else:
            return "Unknown function.", memory
    else:
        memory.append({"role": "assistant", "content": response["content"]})
        return response["content"], memory
