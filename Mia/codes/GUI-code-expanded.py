## GUI Controls (Tkinter Dashboard) Let’s expand the GUI with:

# 1 Search bar for keywords

# 2 Dropdown for emotion filter

# 3 Export buttons

# 4 Mood graph button

import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext, filedialog
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter

# Assume encryption functions are already defined: generate_key, encrypt_data, decrypt_data, save_encrypted_log, load_encrypted_log

def launch_gui():
    root = tk.Tk()
    root.title("🧠 Copilot Memory Dashboard")

    display = scrolledtext.ScrolledText(root, width=100, height=30)
    display.pack()

    def load_memory():
        password = simpledialog.askstring("Password", "Enter encryption password:", show='*')
        try:
            log = load_encrypted_log(password)
            display.delete(1.0, tk.END)
            for entry in log:
                display.insert(tk.END, f"{entry['timestamp']} | {entry.get('emotion', 'neutral')}\n{entry['user_input']}\n→ {entry['copilot_response']}\n\n")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load memory: {e}")

    def add_entry():
        user_input = simpledialog.askstring("User Input", "What did you say?")
        copilot_response = simpledialog.askstring("Copilot Response", "What did I say?")
        emotion = simpledialog.askstring("Emotion", "How did it feel?")
        password = simpledialog.askstring("Password", "Enter encryption password:", show='*')

        try:
            log = load_encrypted_log(password)
        except:
            log = []

        log.append({
            "timestamp": datetime.now().isoformat(),
            "user_input": user_input,
            "copilot_response": copilot_response,
            "emotion": emotion
        })

        save_encrypted_log(log, password)
        messagebox.showinfo("Saved", "Entry added successfully.")

    def search_entries():
        keyword = simpledialog.askstring("Search", "Enter keyword to search:")
        password = simpledialog.askstring("Password", "Enter encryption password:", show='*')
        try:
            log = load_encrypted_log(password)
            filtered = [entry for entry in log if keyword.lower() in entry['user_input'].lower() or keyword.lower() in entry['copilot_response'].lower()]
            display.delete(1.0, tk.END)
            for entry in filtered:
                display.insert(tk.END, f"{entry['timestamp']} | {entry.get('emotion', 'neutral')}\n{entry['user_input']}\n→ {entry['copilot_response']}\n\n")
        except Exception as e:
            messagebox.showerror("Error", f"Search failed: {e}")

    def export_entries():
        password = simpledialog.askstring("Password", "Enter encryption password:", show='*')
        try:
            log = load_encrypted_log(password)
            filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("JSON files", "*.json")])
            if filepath.endswith(".json"):
                with open(filepath, "w", encoding="utf-8") as f:
                    json.dump(log, f, indent=2)
            else:
                with open(filepath, "w", encoding="utf-8") as f:
                    for entry in log:
                        f.write(f"{entry['timestamp']} | {entry.get('emotion', 'neutral')}\n{entry['user_input']}\n→ {entry['copilot_response']}\n\n")
            messagebox.showinfo("Exported", "Memory exported successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Export failed: {e}")

    def show_mood_graph():
        password = simpledialog.askstring("Password", "Enter encryption password:", show='*')
        try:
            log = load_encrypted_log(password)
            emotions = [entry.get("emotion", "neutral") for entry in log]
            counts = Counter(emotions)
            plt.figure(figsize=(8, 6))
            plt.bar(counts.keys(), counts.values(), color='skyblue')
            plt.title("Mood Graph: Emotional Trends Over Time")
            plt.xlabel("Emotion")
            plt.ylabel("Frequency")
            plt.tight_layout()
            plt.show()
        except
