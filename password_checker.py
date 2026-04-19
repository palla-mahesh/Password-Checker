import tkinter as tk
from tkinter import messagebox, ttk
import re
import random
import string

# ---------------- Strength Logic ---------------- #
def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    return score


# ---------------- Suggestions ---------------- #
def suggest_password(password):
    suggestions = []

    if len(password) < 8:
        suggestions.append("Use at least 8 characters")
    if not re.search(r"[A-Z]", password):
        suggestions.append("Add uppercase letters")
    if not re.search(r"[a-z]", password):
        suggestions.append("Add lowercase letters")
    if not re.search(r"[0-9]", password):
        suggestions.append("Include numbers")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("Include special characters")

    return suggestions


# ---------------- Evaluate ---------------- #
def evaluate_password():
    password = entry.get()

    if not password:
        messagebox.showerror("Error", "Enter a password!")
        return

    score = check_strength(password)

    # Strength result + progress bar
    if score <= 2:
        result, color, value = "Weak ❌", "red", 30
    elif score <= 4:
        result, color, value = "Medium ⚠️", "orange", 60
    else:
        result, color, value = "Strong ✅", "green", 100

    result_label.config(text=result, fg=color)
    progress['value'] = value

    # Suggestions
    suggestions = suggest_password(password)
    if suggestions:
        suggestion_text.set("\n".join(suggestions))
    else:
        suggestion_text.set("Good password 👍")


# ---------------- Show/Hide ---------------- #
def toggle_password():
    if entry.cget('show') == '*':
        entry.config(show='')
        toggle_btn.config(text="Hide 👁️")
    else:
        entry.config(show='*')
        toggle_btn.config(text="Show 👁️")


# ---------------- Generate Password ---------------- #
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(chars) for _ in range(12))

    entry.delete(0, tk.END)
    entry.insert(0, password)


# ---------------- Clear ---------------- #
def clear_all():
    entry.delete(0, tk.END)
    result_label.config(text="")
    progress['value'] = 0
    suggestion_text.set("")


# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("Advanced Password Checker 🔐")
root.geometry("450x400")
root.config(bg="#1e1e2f")

title = tk.Label(root, text="Password Strength Checker",
                 font=("Arial", 16, "bold"),
                 bg="#1e1e2f", fg="white")
title.pack(pady=10)

tk.Label(root, text="Enter Password:", bg="#1e1e2f", fg="white").pack()

entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

toggle_btn = tk.Button(root, text="Show 👁️",
                       command=toggle_password,
                       bg="#607d8b", fg="white")
toggle_btn.pack(pady=3)

tk.Button(root, text="Generate Password 🔑",
          command=generate_password,
          bg="#9c27b0", fg="white").pack(pady=5)

tk.Button(root, text="Check Strength",
          command=evaluate_password,
          bg="#4CAF50", fg="white").pack(pady=5)

# Progress Bar
progress = ttk.Progressbar(root, length=300, mode='determinate')
progress.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"),
                        bg="#1e1e2f")
result_label.pack()

# Suggestions display
suggestion_text = tk.StringVar()
suggestion_label = tk.Label(root, textvariable=suggestion_text,
                           bg="#1e1e2f", fg="#ffcc00")
suggestion_label.pack(pady=10)

tk.Button(root, text="Clear",
          command=clear_all,
          bg="#f44336", fg="white").pack(pady=10)

# Run App
root.mainloop()