from agent import run_agent

if __name__ == "__main__":
    memory = [{"role": "system", "content": "You are a smart AI agent with tool use ability."}]
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            break
        response, memory = run_agent(user_input, memory)
        print("Agent:", response)
