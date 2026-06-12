import tkinter as tk
from tkinter import scrolledtext
from chat import ask_groq

print("Loading GUI File...")

print("GUI FILE IS RUNNING")
def send_messages(event=None):
    user_input = entry.get()
    if not user_input.strip():
        return
    
    chatbox.insert(tk.END, "You: ", "you_tag")
    chatbox.insert(tk.END, f"{user_input}\n")
    entry.delete(0, tk.END)

    ai_response = ask_groq(user_input)
    chatbox.insert(tk.END, "AI: ", "ai_tag")
    chatbox.insert(tk.END, f"{ai_response}\n\n")
    chatbox.see(tk.END)

root = tk.Tk()
root.title("AI, but rude.")

chatbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Segoe UI", 10))
chatbox.pack(padx=10, pady=10, expand=True)
chatbox.tag_config("you_tag", foreground="cyan")
chatbox.tag_config("ai_tag", foreground="magenta")

bottom_frame = tk.Frame(root)
bottom_frame.pack(side="left", fill="x", expand=True)

entry = tk.Entry(bottom_frame, width=50, font=("Segoe UI", 10))
entry.pack(side=tk.LEFT, padx=10, pady=10)

send_button = tk.Button(bottom_frame, text="Send", command=send_messages, font=("Segoe UI", 10))
send_button.pack(side=tk.LEFT, pady=10)

entry.bind("<Return>", send_messages)

root.mainloop()