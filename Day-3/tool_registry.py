from tools import calculator

TOOLS = {
    'calculator':calculator.run
}

def call_tool(tool_name:str, input_text:str) -> str:
    if tool_name in TOOLS:
        return TOOLS[tool_name](input_text)
    else:
        return f"No tool named '{tool_name}' found."