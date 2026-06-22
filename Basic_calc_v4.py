# Calculator v4 - Menu Driven with History

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

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error: Cannot find square root of a negative number!"
    return a ** 0.5

history = []  # list to store past calculations

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
            result = square_root(num1)
            print("Result:", result)
            history.append(f"sqrt({num1}) = {result}")
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
                op_symbol = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                op_symbol = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                op_symbol = "*"
            elif choice == "4":
                result = divide(num1, num2)
                op_symbol = "/"
            elif choice == "5":
                result = power(num1, num2)
                op_symbol = "^"

            print("Result:", result)
            history.append(f"{num1} {op_symbol} {num2} = {result}")

    except ValueError:
        print("Error: Please enter valid numbers!")