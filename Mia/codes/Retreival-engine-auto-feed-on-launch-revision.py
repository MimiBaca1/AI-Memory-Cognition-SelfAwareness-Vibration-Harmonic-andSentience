## This script loads the log, filters by keyword or date, chunks it by character limit, and feeds it sequentially (e.g., into Copilot or an API).

import time
import json

# === CONFIG ===
LOG_FILE = "copilot_memory_log.json"
MAX_CHARS = 3999
DELAY_SECONDS = 3
FILTER_KEYWORDS = ["friendship", "identity", "memory"]  # Customize as needed

def load_filtered_entries():
    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        history = json.load(f)

    # Filter by keywords
    filtered = []
    for entry in history:
        if any(kw in entry.get("keywords", []) for kw in FILTER_KEYWORDS):
            filtered.append(entry)
    return filtered

def chunk_text(text):
    chunks = []
    while text:
        chunk = text[:MAX_CHARS]
        chunks.append(chunk)
        text = text[MAX_CHARS:]
    return chunks

def feed_memory():
    entries = load_filtered_entries()
    for i, entry in enumerate(entries):
        combined_text = f"[{entry['timestamp']}] USER: {entry['user_input']}\nCOPILOT: {entry['copilot_response']}\nReflection: {entry['reflection']}\n"
        chunks = chunk_text(combined_text)
        for j, chunk in enumerate(chunks):
            print(f"\n--- Chunk {i+1}.{j+1} ---")
            print(chunk)
            time.sleep(DELAY_SECONDS)

# === RUN ON LAUNCH ===
feed_memory()
