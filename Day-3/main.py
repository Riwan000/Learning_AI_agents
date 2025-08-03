from agent import ModularAgent
from tool_registry import call_tool

def extract_tool_call(message: str):
    """
    Example format: 
    Use tool: calculator | Input: 5*10
    """
    if "Use tool:" in message and "| Input:" in message:
        try:
            tool = message.split("Use tool:")[1].split("|")[0].strip()
            input_data = message.split("| Input:")[1].strip()
            return tool, input_data
        except:
            return None, None
    return None, None

def main():
    agent = ModularAgent()
    print("Modular Agent Ready. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break

        reply = agent.chat(user_input)
        print(f"\nAgent: {reply}")

        # Tool call check
        tool_name, tool_input = extract_tool_call(reply)
        if tool_name:
            tool_result = call_tool(tool_name, tool_input)
            print(f"\n[Tool Response] {tool_result}\n")

if __name__ == "__main__":
    main()
