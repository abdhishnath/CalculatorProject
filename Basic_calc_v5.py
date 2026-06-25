# Calculator v6 - Added history and backspace feature
# Transition from terminal calculator to GUI design

import tkinter as tk
from tkinter import messagebox
from math import sqrt

history = []


class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): return "Error" if b == 0 else a / b
    def power(self, a, b): return a ** b
    def square_root(self, a): return "Error" if a < 0 else sqrt(a)


calc = Calculator()

# GUI setup
root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")

# Entry display
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
        for op in ["+", "-", "*", "/"]:
            if op in expression[1:]:  # skip index 0 in case of negative number
                num1_str, num2_str = expression.split(op, 1)
                num1, num2 = float(num1_str), float(num2_str)

                if op == "+":
                    result = calc.add(num1, num2)
                elif op == "-":
                    result = calc.subtract(num1, num2)
                elif op == "*":
                    result = calc.multiply(num1, num2)
                elif op == "/":
                    result = calc.divide(num1, num2)

                history.append(f"{expression} = {result}")
                entry.delete(0, tk.END)
                entry.insert(0, str(result))
                return

        entry.delete(0, tk.END)
        entry.insert(0, "Error")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def show_history():
    if len(history) == 0:
        messagebox.showinfo("History", "No calculations done yet!")
    else:
        messagebox.showinfo("History", "\n".join(history))


# Buttons layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
    ("C", 5, 0), ("⌫", 5, 1), ("^", 5, 2), ("V", 5, 3),
    ("History", 6, 0)
]

for (text, row, col) in buttons:
    if text == "=":
        action = calculate
    elif text == "C":
        action = clear_entry
    elif text == "⌫":
        action = backspace
    elif text == "V":
        action = lambda: entry.insert(tk.END, "**0.5")
    elif text == "^":
        action = lambda: entry.insert(tk.END, "**")
    elif text == "History":
        action = show_history
    else:
        action = lambda val=text: click_button(val)

    if text == "History":
        tk.Button(root, text=text, width=24, height=2, command=action).grid(
            row=row, column=0, columnspan=4, padx=5, pady=5
        )
    else:
        tk.Button(root, text=text, width=5, height=2, command=action).grid(
            row=row, column=col, padx=5, pady=5)

root.mainloop()