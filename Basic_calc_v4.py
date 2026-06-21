# Calculator v4 - Menu Driven

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

while True:
    print("\n----- CALCULATOR MENU -----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (a^b)")
    print("6. Square Root (of one number)")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "7":
        print("Thank you for using the calculator!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice! Please select between 1-7.")
        continue

    try:
        if choice == "6":
            num1 = float(input("Enter the number: "))
            print("Result:", square_root(num1))
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(num1, num2))
            elif choice == "2":
                print("Result:", subtract(num1, num2))
            elif choice == "3":
                print("Result:", multiply(num1, num2))
            elif choice == "4":
                print("Result:", divide(num1, num2))
            elif choice == "5":
                print("Result:", power(num1, num2))

    except ValueError:
        print("Error: Please enter valid numbers!")