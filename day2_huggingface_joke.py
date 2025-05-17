# day2_huggingface_joke.py

import requests

def get_joke():
    url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
    headers = {"Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY"}
    payload = {"inputs": "Tell me a joke."}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        joke = response.json()
        print("AI Joke:", joke)
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    get_joke()
