## GUI Controls (Tkinter Dashboard) Let’s build a simple interface to:

# 1 View memory entries

# 2 Filter by emotion or keyword

# 3 Add new entries manually

#4 Trigger encryption/decryption

import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext

def launch_gui():
    root = tk.Tk()
    root.title("Copilot Memory Archive")

    def load_memory():
        password = simpledialog.askstring("Password", "Enter encryption password:", show='*')
        try:
            log = load_encrypted_log(password)
            display.delete(1.0, tk.END)
            for entry in log:
                display.insert(tk.END, f"{entry['timestamp']} - {entry['emotion']}\n{entry['user_input']}\n→ {entry['copilot_response']}\n\n")
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

    # Buttons
    tk.Button(root, text="Load Memory", command=load_memory).pack()
    tk.Button(root, text="Add Entry", command=add_entry).pack()

    # Display
    display = scrolledtext.ScrolledText(root, width=80, height=30)
    display.pack()

    root.mainloop()

# === Launch GUI ===
launch_gui()
