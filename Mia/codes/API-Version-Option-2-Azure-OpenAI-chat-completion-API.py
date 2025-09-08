API_URL = 'https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT_NAME/chat/completions?api-version=2023-07-01-preview'
API_KEY = 'YOUR_AZURE_API_KEY'

HEADERS = {
    'api-key': API_KEY,
    'Content-Type': 'application/json'
}

def send_to_azure(chunk):
    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": chunk}
        ]
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        reply = response.json()
        print("✅ Azure Response:", reply["choices"][0]["message"]["content"])
    else:
        print(f"❌ Azure Error {response.status_code}: {response.text}")
