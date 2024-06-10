import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate the password
def generate_password():
    length = int(length_entry.get())
    
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Display the password
    messagebox.showinfo("Generated Password", f"Your generated password is:\n{password}")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
tk.Label(root, text="Password Length:").pack(pady=25)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)
length_entry.insert(0, "15")  # Default length

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=20)

# Run the main event loop
root.mainloop()
