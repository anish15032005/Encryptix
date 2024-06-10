import tkinter as tk
from tkinter import messagebox

# Define the arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Function to perform the selected operation and display the result
def perform_operation():
    try:
        num1 = float(entry1.get())  # Get the first number from the entry widget
        num2 = float(entry2.get())  # Get the second number from the entry widget
        choice = operation_var.get()  # Get the selected operation
        
        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "/"
        else:
            result = "Invalid operation"
            operation = ""
        
        result_label.config(text=f"{num1} {operation} {num2} = {result}")  # Display the result
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")  # Show error message if input is invalid

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place the widgets
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Create a variable to store the selected operation
operation_var = tk.StringVar()
operation_var.set("1")  # Set default operation to "Add"

# Create and place the option menu for selecting the operation
tk.Label(root, text="Select operation:").grid(row=2, column=0, padx=10, pady=5)
operations = [("Add", "1"), ("Subtract", "2"), ("Multiply", "3"), ("Divide", "4")]
for operation, value in operations:
    tk.Radiobutton(root, text=operation, variable=operation_var, value=value).grid(sticky='W', padx=10)

# Create and place the button to perform the operation
tk.Button(root, text="Calculate", command=perform_operation).grid(row=3, column=0, columnspan=2, pady=10)

# Create and place the label to display the result
result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, columnspan=2)

# Run the main event loop
root.mainloop()
