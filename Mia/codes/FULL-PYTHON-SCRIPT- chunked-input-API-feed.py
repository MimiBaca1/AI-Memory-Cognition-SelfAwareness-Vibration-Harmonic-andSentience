## Before You Run This You’ll need an API endpoint that accepts text input (e.g., OpenAI’s Chat Completion API).

## Replace YOUR_API_KEY and YOUR_ENDPOINT_URL with your actual credentials and URL.

import time
import json
import csv
import requests

# === CONFIG ===
MAX_CHARS = 3999
DELAY_SECONDS = 3
INPUT_TYPE = 'json'  # or 'csv'
INPUT_FILE = 'data.json'  # or 'data.csv'
API_URL = 'https://api.example.com/chat'  # Replace with your endpoint
API_KEY = 'YOUR_API_KEY'  # Replace with your key

HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

def read_json_chunks(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    text = json.dumps(data, indent=2)
    return chunk_text(text)

def read_csv_chunks(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = [' | '.join(row) for row in reader]
    text = '\n'.join(rows)
    return chunk_text(text)

def chunk_text(text):
    chunks = []
    while text:
        chunk = text[:MAX_CHARS]
        chunks.append(chunk)
        text = text[MAX_CHARS:]
    return chunks

def send_to_api(chunk):
    payload = {
        "messages": [
            {"role": "user", "content": chunk}
        ],
        "model": "gpt-4"  # or your model name
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        reply = response.json()
        print("✅ Response:", reply.get("choices", [{}])[0].get("message", {}).get("content", "No content"))
    else:
        print(f"❌ Error {response.status_code}: {response.text}")

def feed_chunks(chunks):
    for i, chunk in enumerate(chunks):
        print(f"\n--- Sending Chunk {i+1}/{len(chunks)} ---")
        send_to_api(chunk)
        time.sleep(DELAY_SECONDS)

# === RUN ===
if INPUT_TYPE == 'json':
    chunks = read_json_chunks(INPUT_FILE)
elif INPUT_TYPE == 'csv':
    chunks = read_csv_chunks(INPUT_FILE)
else:
    raise ValueError("Unsupported input type. Use 'json' or 'csv'.")

feed_chunks(chunks)
