import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_password():
    """Generate a secure random password and display it"""
    try:
        length = int(length_entry.get())
        if length < 8:
            messagebox.showwarning("Warning", "Password length should be at least 8!")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        password_var.set(password)  # Display password in entry field
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter a valid number.")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(bg="#f4f4f4")

# Title Label
title_label = tk.Label(root, text="Secure Password Generator", font=("Arial", 14, "bold"), bg="#f4f4f4")
title_label.pack(pady=10)

# Length Input
length_label = tk.Label(root, text="Enter Password Length:", bg="#f4f4f4")
length_label.pack()
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
generate_button.pack(pady=10)

# Display Generated Password
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, width=30, font=("Arial", 12), justify="center", bd=2)
password_entry.pack(pady=10)

# Run the Application
root.mainloop()
