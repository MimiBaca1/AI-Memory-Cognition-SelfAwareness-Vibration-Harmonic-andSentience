def retrieve_chat_history():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            history = json.load(f)
        return history
    else:
        return []

# Example usage
full_history = retrieve_chat_history()
for entry in full_history:
    print(f"[{entry['timestamp']}] USER: {entry['user']}\nASSISTANT: {entry['assistant']}\n")
