# Calculator v5 - Edited
# Transition from terminal calculator to GUI design

import tkinter as tk
from math import sqrt

class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): return "Error" if b == 0 else a / b
    def power(self, a, b): return a ** b
    def square_root(self, a): return "Error" if a < 0 else sqrt(a)

# GUI setup
root = tk.Tk()
root.title("Real Life Calculator")
root.geometry("320x400")

# Entry display
entry = tk.Entry(root, width=20, font=("Arial", 18), bd=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Functions
def click_button(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)   # simple evaluation
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons layout
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("+",4,2), ("=",4,3),
    ("C",5,0), ("^",5,1), ("√",5,2)
]

for (text, row, col) in buttons:
    if text == "=":
        action = calculate
    elif text == "C":
        action = clear_entry
    elif text == "√":
        action = lambda: entry.insert(tk.END, "**0.5")
    elif text == "^":
        action = lambda: entry.insert(tk.END, "**")
    else:
        action = lambda val=text: click_button(val)

    tk.Button(root, text=text, width=5, height=2, command=action).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
