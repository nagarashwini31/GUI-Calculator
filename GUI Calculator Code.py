import tkinter as tk

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for the calculator display
entry = tk.Entry(root, width=25, font=("Arial", 14), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Add buttons to the grid
for text, row, col in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 12),
                           command=calculate)
    elif text == "C":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 12),
                           command=clear_entry)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 12),
                           command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the main loop
root.mainloop()
