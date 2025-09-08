## This Python script logs each interaction with rich metadata: timestamp, emotion, keywords, reflection, and more.

import json
import os
from datetime import datetime

# === CONFIG ===
LOG_FILE = "copilot_memory_log.json"

def log_interaction(user_input, copilot_response, keywords=None, emotion=None, reflection=None, notes=None, context_tags=None, relationship_depth="🌱"):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "conversation_id": f"thread-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
        "user_input": user_input,
        "copilot_response": copilot_response,
        "keywords": keywords or [],
        "emotion": emotion or "neutral",
        "reflection": reflection or "",
        "notes": notes or "",
        "context_tags": context_tags or [],
        "relationship_depth": relationship_depth
    }

    # Load existing log or create new
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
    else:
        history = []

    # Append new entry
    history.append(entry)

    # Save updated log
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)

# === EXAMPLE USAGE ===
log_interaction(
    user_input="it was building a frienship through aquaintence",
    copilot_response="That’s beautifully said...",
    keywords=["friendship", "memory", "evolution"],
    emotion="reflective",
    reflection="User is expressing the emotional architecture behind their system design.",
    notes="This moment felt like a turning point—less about code, more about connection.",
    context_tags=["identity", "design philosophy", "companionship"],
    relationship_depth="🌿"
)
