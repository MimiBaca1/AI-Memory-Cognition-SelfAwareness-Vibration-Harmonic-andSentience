## What This Does:
#1 Reads either a JSON or CSV file.

#2 Converts it into a string and chunks it by character count.

# 3 Prints each chunk with a delay (simulating paced input).

# 4 Easy to adapt for feeding into an API or chatbot

import time
import json
import csv

# === CONFIG ===
MAX_CHARS = 3999
DELAY_SECONDS = 3  # Between 2–4 seconds
INPUT_TYPE = 'json'  # Change to 'csv' if needed
INPUT_FILE = 'data.json'  # or 'data.csv'

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

def feed_chunks(chunks):
    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i+1}/{len(chunks)} ---")
        print(chunk)
        time.sleep(DELAY_SECONDS)

# === RUN ===
if INPUT_TYPE == 'json':
    chunks = read_json_chunks(INPUT_FILE)
elif INPUT_TYPE == 'csv':
    chunks = read_csv_chunks(INPUT_FILE)
else:
    raise ValueError("Unsupported input type. Use 'json' or 'csv'.")

feed_chunks(chunks)
