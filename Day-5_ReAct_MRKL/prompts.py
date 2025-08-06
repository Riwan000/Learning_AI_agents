system_prompt = """
You are a reasoning assistant that decides whether to respond directly or use a tool.
Tools available:
1. calculator(expression)
2. web_search(query)

Use step-by-step reasoning (ReAct style).
"""

tool_prompt_template = """Thought: {thought}
Action: {tool_name}
Action Input: {tool_input}
"""

final_prompt_template = """Thought: {thought}
Answer: {final_answer}
"""
