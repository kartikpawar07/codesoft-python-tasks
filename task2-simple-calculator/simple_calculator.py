def calculator():
    print("Welcome to Simple Calculator\n")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    print("\nChoose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Enter choice (1/2/3/4): ")
    if choice == '1':
        result = num1 + num2
        op = "+"
    elif choice == '2':
        result = num1 - num2
        op = "-"
    elif choice == '3':
        result = num1 * num2
        op = "*"
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            op = "/"
        else:
            print("Error: Cannot divide by zero.")
            return
    else:
        print("Invalid operation choice.")
        return
    print(f"\nResult: {num1} {op} {num2} = {result}")
# Run the calculator
calculator()
