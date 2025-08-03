# Day 3: Modular Agent with Tool Calling (OpenRouter)

## 🧠 Goal

Build a modular AI agent using OpenRouter that:
- Maintains conversation history (memory)
- Uses tools based on user input (tool calling)
- Automatically triggers tools when needed

## 🗂️ Folder Structure

```
day3_modular_agent/
│
├── tools/
│   └── calculator.py          # Tool for basic math operations
│
├── agent.py                   # Core logic to decide tool usage and call the model
├── main.py                    # User interface to interact with the agent
├── tool_registry.py           # Registry to map tool names to functions
├── .env                       # Stores the OpenRouter API key securely
└── README_day3.md             # This file
```

## 🧩 Tools

- **Calculator Tool** (`tools/calculator.py`): Handles simple arithmetic expressions like `2 + 2`.

## 🚀 How It Works

1. **User gives input** → The agent appends it to message history.
2. **OpenRouter API** → Sends conversation + system prompt to determine if a tool is needed.
3. **Tool Auto-triggering** → If the agent responds with something like `use tool calculator`, the tool is executed.
4. **Response** → The result is returned as part of the conversation.

## 🛠️ Setup

1. Clone the repo or copy the folder.

2. Install required packages (optional if using basic `requests` only):
```
pip install python-dotenv requests
```

3. Create a `.env` file:
```
OPENROUTER_API_KEY=your_openrouter_key_here
```

4. Run the agent:
```
python main.py
```

## 🧪 Example Interaction

```
You: what is 2 + 5

Agent: 2 + 5 = 7

You: use tool calculator

Agent: I'll use the calculator tool to find 2 + 5.
Agent: 2 + 5 = 7
```

## ⚙️ Extending Tools

Add more tools by:
1. Writing a new tool function in `tools/`.
2. Registering it in `tool_registry.py`.
3. Prompting the model to use the tool in your `agent.py` logic.

---

**Next Step → Day 4:** Add function calling support using structured schemas.