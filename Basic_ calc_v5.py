# Calculator v5 - Part A: OOP Structure (still terminal-based)

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero!"
        return a / b

    def power(self, a, b):
        return a ** b

    def square_root(self, a):
        if a < 0:
            return "Error: Cannot find square root of a negative number!"
        return a ** 0.5


calc = Calculator()  # creating an object of the Calculator class
history = []

while True:
    print("\n----- CALCULATOR MENU -----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (a^b)")
    print("6. Square Root (of one number)")
    print("7. View History")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "8":
        print("Thank you for using the calculator!")
        break

    if choice == "7":
        if len(history) == 0:
            print("No calculations done yet!")
        else:
            print("\n----- CALCULATION HISTORY -----")
            for i, record in enumerate(history, start=1):
                print(f"{i}. {record}")
        continue

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice! Please select between 1-8.")
        continue

    try:
        if choice == "6":
            num1 = float(input("Enter the number: "))
            result = calc.square_root(num1)
            print("Result:", result)
            history.append(f"sqrt({num1}) = {result}")
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = calc.add(num1, num2)
                op_symbol = "+"
            elif choice == "2":
                result = calc.subtract(num1, num2)
                op_symbol = "-"
            elif choice == "3":
                result = calc.multiply(num1, num2)
                op_symbol = "*"
            elif choice == "4":
                result = calc.divide(num1, num2)
                op_symbol = "/"
            elif choice == "5":
                result = calc.power(num1, num2)
                op_symbol = "^"

            print("Result:", result)
            history.append(f"{num1} {op_symbol} {num2} = {result}")

    except ValueError:
        print("Error: Please enter valid numbers!")