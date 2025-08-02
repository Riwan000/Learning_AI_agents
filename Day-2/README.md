# 🧠 Day 2: AI Agent with Basic Memory

## 🚀 Objective

Create an AI agent that:
- Maintains memory of previous conversation turns.
- Supports stateful interaction (context-aware).
- Uses OpenRouter API and a selected open-source model.
- Prepares the groundwork for integrating tools in future steps.

---

## 🗂️ Project Structure

```
day2_memory_agent/
│
├── .env                  # Contains OPENROUTER_API_KEY
├── day2_agent.py         # Main agent script
└── README.md             # This file
```

---

## 🔧 Setup

### 1. Install dependencies

```bash
pip install python-dotenv requests
```

### 2. Create `.env` file

```env
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Replace with your actual API key from [https://openrouter.ai](https://openrouter.ai)

---

## 💡 How It Works

The agent:

1. Loads a system prompt that defines its role.
2. Stores every user and assistant message in a `messages` list.
3. Sends the full message history to the OpenRouter endpoint each time.
4. Receives model responses that reflect prior context and state.

---

## 🧪 Example Usage

```bash
$ python day2_agent.py
Agent is ready. Type 'exit' to quit.

You : Hello, who are you?
Agent: I am your helpful assistant.

You : What's my name?
Agent: You haven't told me your name yet. What is it?

You : I'm Riwano.
Agent: Nice to meet you, Riwano.
```

---

## 🧱 Code Highlights

- ✅ **Memory** is preserved using a `messages` list that grows with each interaction.
- ✅ **System prompt** is included only once at the beginning.
- ✅ Uses `glm-4.5-air:free` model via OpenRouter API.

---

## ⚙️ Customization

You can customize the model by changing this line in `day2_agent.py`:

```python
MODEL = "z-ai/glm-4.5-air:free"
```

To other supported models from [https://openrouter.ai/docs](https://openrouter.ai/docs).

---

## 🛠️ Next Steps (Day 3 Teaser)

In **Day 3**, we’ll:
- Add tools (like a calculator)
- Teach the agent to **call tools automatically**
- Simulate tool-use logic for real-world agents

---

## 📌 Learnings

- Conversation history enables dynamic, personalized AI responses.
- Memory is just structured message history — no complex vector DBs needed yet.
- This architecture is extendable and critical for building agents with state, tools, or RAG.