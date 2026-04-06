import os
from dotenv import load_dotenv
import requests

# Load .env file
load_dotenv()

base_url = os.getenv("TOKEN")

print("BASE URL:", base_url)

url = base_url + "/chat/completions"

headers = {
    "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Hello"}]
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.text)