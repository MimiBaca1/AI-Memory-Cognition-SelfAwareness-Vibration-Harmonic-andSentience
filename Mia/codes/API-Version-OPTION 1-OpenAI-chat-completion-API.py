API_URL = 'https://api.openai.com/v1/chat/completions'
API_KEY = 'YOUR_OPENAI_API_KEY'

HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

def send_to_openai(chunk):
    payload = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": chunk}
        ]
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        reply = response.json()
        print("✅ OpenAI Response:", reply["choices"][0]["message"]["content"])
    else:
        print(f"❌ OpenAI Error {response.status_code}: {response.text}")
