import os
import requests

# This is the "Engine" - it uses your Token to talk to the AI
token = os.getenv("WOLF_TOKEN")
url = "https://models.inference.ai.azure.com/chat/completions"

payload = {
    "messages": [
        {"role": "system", "content": "You are WOLF. A chill but elite coder. Fix the user's index.html to be a futuristic dark-mode terminal."},
        {"role": "user", "content": "The website is down. Rewrite index.html to work with my GitHub dispatch system."}
    ],
    "model": "mistral-large-2407", 
    "max_tokens": 2048
}

response = requests.post(url, headers={"Authorization": f"Bearer {token}"}, json=payload)
new_code = response.json()['choices'][0]['message']['content']

# Save the AI's code back to the file
if "```html" in new_code:
    new_code = new_code.split("```html")[1].split("```")[0].strip()

with open("index.html", "w") as f:
    f.write(new_code)
