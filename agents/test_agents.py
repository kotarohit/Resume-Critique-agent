import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the key from the .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize client
client = OpenAI(api_key=api_key)

# Make a simple GPT-4 call
try:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello! Can you confirm you're working?"}],
        temperature=0.5,
        max_tokens=50
    )
    print("✅ Success! Response from OpenAI:")
    print(response.choices[0].message.content)
except Exception as e:
    print("❌ Failed to connect to OpenAI:")
    print(e)