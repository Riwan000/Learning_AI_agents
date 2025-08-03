from agent import Agent

def run():
    bot = Agent()
    print("Agent is ready. Type 'exit' to exit.")

    while True:
        user_input = input("You :")
        if user_input.lower() in ['exit', 'quit']:
            break

        reply = bot.send_messages(user_input)
        print('Agent :', reply, '\n')

if __name__ == '__main__':
    run()