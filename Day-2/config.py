# Configurations of the agent.

import os 
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv("OPENROUTER_API_KEY") # GEtting the api key from the env file.
API_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "Day2-Agent"
}

MODEL = "z-ai/glm-4.5-air:free"