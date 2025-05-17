import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

from agents.orches import orchestrate

if __name__ == "__main__":
    orchestrate()