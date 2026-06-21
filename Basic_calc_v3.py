# Calculator v3 - Functions + Loop

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

while True:
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            print("Result:", add(num1, num2))
        elif op == "-":
            print("Result:", subtract(num1, num2))
        elif op == "*":
            print("Result:", multiply(num1, num2))
        elif op == "/":
            print("Result:", divide(num1, num2))
        else:
            print("Invalid Operator!")

    except ValueError:
        print("Error: Please enter valid numbers!")

    again = input("\nDo you want to calculate again? (y/n): ")
    if again.lower() != "y":
        print("Thank you for using the calculator!")
        break