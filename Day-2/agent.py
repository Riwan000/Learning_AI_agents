import requests 
from config import API_URL, HEADERS, MODEL
from prompts import SYSTEM_PROMPT

class Agent:
    def __init__(self):
        self.messages = [{"role" : "system", "content" : SYSTEM_PROMPT}]

    def send_messages(self, user_input):
        self.messages.append({"role" : "system", "content" : user_input})

        data = {
            "model" : MODEL,
            "messages" : self.messages
        }

        try:
            response = requests.post(API_URL, headers=HEADERS, json=data)
            response.raise_for_status()
            result = response.json()

            reply = result['choices'][0]['message']['content']
            self.messages.append({'role' : 'assistant', 'content' : reply})
            return reply

        except Exception as e:
            print("Request failed:", e)
            if response is not None:
                print("Raw response:", response.text)
            return "Sorry, something went wrong."

