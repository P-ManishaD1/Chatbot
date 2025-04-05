# Function to handle question asking
def ask_question():
    user_question = question_entry.get().strip()
    if not user_question:
        messagebox.showwarning("Input Error", "Please enter a question.")
        return
    answer = get_response(user_question)
    answer_label.config(text=f"Bot's Answer:\n{answer}", bg="#e0f7fa")
    question_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("500x400")
root.config(bg="#f1f8e9")

# Title Label
title_label = tk.Label(root, text="Welcome to AI Chatbot", font=("Helvetica", 18, "bold"), bg="#a5d6a7", fg="#1b5e20", pady=10)
title_label.pack(fill=tk.X)

# Ask Label
ask_label = tk.Label(root, text="Enter your question below:", font=("Arial", 12), bg="#f1f8e9", fg="#2e7d32")
ask_label.pack(pady=(20, 5))

# Entry widget for question
question_entry = tk.Entry(root, font=("Arial", 12), width=50, bd=2, relief=tk.GROOVE)
question_entry.pack(pady=5)
question_entry.bind("<Return>", lambda event: ask_question())

# Ask button
ask_button = tk.Button(root, text="Get Answer", font=("Arial", 12), bg="#66bb6a", fg="white", padx=10, pady=5, command=ask_question)
ask_button.pack(pady=10)

# Answer Label
answer_label = tk.Label(root, text="Bot's Answer will appear here.", font=("Arial", 12), bg="#fffde7", fg="#4e342e", wraplength=450, justify="left", bd=2, relief=tk.RIDGE, padx=10, pady=10)
answer_label.pack(pady=20, fill=tk.BOTH, expand=True, padx=20)

# Start the GUI
root.mainloop()
