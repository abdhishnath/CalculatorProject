import tkinter as tk
from tkinter import messagebox
from math import sqrt

# History list
history = []

class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b):
        if b == 0: raise ValueError("Error")
        return a / b

calc = Calculator()

# GUI Setup
root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")

# Entry Display
entry = tk.Entry(root, width=20, font=("Arial", 18), bd=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Functions
def click_button(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    if current:
        entry.delete(len(current)-1, tk.END)

def calculate():
    try:
        expression = entry.get()
        # Real symbols ko code-readable symbols mein badalna
        processed_exp = expression.replace("×", "*").replace("÷", "/").replace("−", "-")
        
        # Calculation
        result = eval(processed_exp)
        
        # History mein save karna
        history.append(f"{expression} = {result}")
        
        # Display result
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def show_history():
    if not history:
        messagebox.showinfo("History", "No calculations done yet!")
    else:
        messagebox.showinfo("History", "\n".join(history))

# Buttons Layout
buttons = [
    ("√", 1, 0), ("^", 1, 1), ("C", 1, 2), ("⌫", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("÷", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("×", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("−", 4, 3),
    (".", 5, 0), ("0", 5, 1), ("=", 5, 2), ("+", 5, 3),
    ("History", 6, 0)
]

# Button Generation Loop
for (text, row, col) in buttons:
    if text == "=": action = calculate
    elif text == "C": action = clear_entry
    elif text == "⌫": action = backspace
    elif text == "√": action = lambda: entry.insert(tk.END, "**0.5")
    elif text == "^": action = lambda: entry.insert(tk.END, "**")
    elif text == "History": action = show_history
    else: action = lambda v=text: click_button(v)

    # Layout Rendering
    if text == "History":
        tk.Button(root, text=text, width=24, height=2, command=action).grid(row=row, column=0, columnspan=4, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, height=2, command=action).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()