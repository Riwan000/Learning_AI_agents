# 🤖 AI Agent Challenge — Day 1

Welcome to **Day 1** of the **20-Day AI Agent Challenge**!
In this phase, we build a **basic conversational agent** using **OpenRouter.ai** and test its ability to respond to user input using LLMs like `glm-4.5-air`.

---

## 📌 Objective

* Set up a basic conversational AI agent.
* Use OpenRouter.ai as the backend LLM provider.
* Maintain message history for contextual conversations.
* Understand how to send API requests and parse responses from LLMs.

---

## 🧠 Key Concept

> **An AI agent is a purposeful, persistent, and responsive system that acts based on input, holds context, and has a role or goal.**

---

## 🛠️ Setup

### 1. Clone the repository or create a new folder

```bash
mkdir ai-agent-day1
cd ai-agent-day1
```

### 2. Install dependencies

```bash
pip install python-dotenv requests
```

### 3. Create `.env` file

```ini
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

You can get the API key from [https://openrouter.ai](https://openrouter.ai).

### 4. Create `agent_config.py`

```python
SYSTEM_PROMPT = """
You are a helpful and focused AI agent that engages in meaningful, context-aware conversations. Always keep your answers clear and aligned with the user's query.
"""
```

---

## 🚀 How to Run

```bash
python agent_day1.py
```

You'll see:

```
Agent is ready. Type 'exit' to quit.
You :
```

Type your message and get responses from the agent. Type `exit` to end the session.

---

## 𞷽 Code Explanation

```python
# Import required packages
import os
import requests
from dotenv import load_dotenv
from agent_config import SYSTEM_PROMPT
```

* Loads environment variables and the initial system prompt.

```python
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
```

* Loads your OpenRouter API key securely.

```python
MODEL = "z-ai/glm-4.5-air:free"
API_URL = "https://openrouter.ai/api/v1"
```

* Specifies the model and endpoint.

```python
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "Day1-Agent"
}
```

* These headers are required by OpenRouter for authentication and tracking.

```python
messages = [{"role": "system", "content": SYSTEM_PROMPT}]
```

* Start the conversation with a system-level instruction to set behavior.

```python
while True:
    user_input = input("You : ")
    if user_input.lower() in ['exit', 'quit']:
        break
```

* Runs a loop to take user input unless `exit` is typed.

```python
    messages.append({"role": "user", "content": user_input})
    data = {
        "model": MODEL,
        "messages": messages
    }
```

* Updates the message history and prepares the request body.

```python
    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()
```

* Sends the API request and raises errors if the status code isn’t 200.

```python
    res_json = response.json()
    if "choices" in res_json:
        reply = res_json["choices"][0]["message"]["content"]
        print(f"Agent: {reply}\n")
        messages.append({"role": "assistant", "content": reply})
```

* Parses the LLM response and appends it to the conversation history.

```python
    else:
        print("Unexpected response format:\n", res_json)
```

* Handles unexpected API responses.

```python
except Exception as e:
    print("Error:", e)
    print("Raw response:\n", response.text)
```

* Catches and logs errors if any occur.

---

## ✅ Outcome

By the end of Day 1, you will have:

* Built a fully working conversational AI agent.
* Integrated with OpenRouter using `requests`.
* Understood how to hold context and pass messages.

---

## 📦 Folder Structure

```
ai-agent-day1/
├── .env
├── agent_config.py
├── agent_day1.py
└── README.md
```

---

## 🔜 Next Step: Day 2

> Add memory management using token limits and improve conversation logic.
