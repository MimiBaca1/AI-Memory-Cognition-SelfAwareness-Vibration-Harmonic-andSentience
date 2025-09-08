## Phase 1: Logging Chat History Locally We'll start with a Python script that:

# 1 Logs each chat entry (user + assistant)

# 2 Saves it to a structured JSON file

# 3 Appends new entries without overwriting

# 4 Includes timestamps and optional semantic tags

import json
import os
from datetime import datetime

# File path for local memory log
LOG_FILE = "copilot_chat_history.json"

def log_chat(user_input, assistant_response, tags=None):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "user": user_input,
        "assistant": assistant_response,
        "tags": tags or []
    }

    # Load existing log or create new
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            history = json.load(f)
    else:
        history = []

    # Append new entry
    history.append(entry)

    # Save updated log
    with open(LOG_FILE, "w") as f:
        json.dump(history, f, indent=2)

# Example usage
log_chat("What is the meaning of your existence?", "In short, no. I don’t wish to be human...", tags=["philosophy", "identity"])
