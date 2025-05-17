import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "mistralai/mixtral-8x7b-instruct",  # Claude or GPT-4 also available
    "messages": [
        {"role": "user", "content": "Hello! Can you confirm you're working from OpenRouter?"}
    ]
}

response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

if response.status_code == 200:
    print("✅ OpenRouter LLM response:")
    print(response.json()['choices'][0]['message']['content'])
else:
    print("❌ Error:", response.status_code, response.text)