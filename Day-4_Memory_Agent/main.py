import os
from dotenv import load_dotenv
from agent import run_agent

load_dotenv()

def main():
    print("Agent with memory is ready. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = run_agent(user_input)
        print(f"Agent: {response}\n")

if __name__ == "__main__":
    main()