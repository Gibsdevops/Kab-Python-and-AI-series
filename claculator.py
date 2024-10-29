import tkinter as tk

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            result = num1 / num2 if num2 != 0 else "Error! Division by zero."
        else:
            result = "Invalid operation"
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Invalid input. Please enter numeric values.")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry fields
entry1 = tk.Entry(root)
entry1.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Create buttons for operations
buttons = [
    ("Add", lambda: calculate("Add")),
    ("Subtract", lambda: calculate("Subtract")),
    ("Multiply", lambda: calculate("Multiply")),
    ("Divide", lambda: calculate("Divide")),
]

for (text, command) in buttons:
    button = tk.Button(root, text=text, command=command)
    button.pack(pady=5)

# Result label
label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=5)

# Run the application
root.mainloop()
