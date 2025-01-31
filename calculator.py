def calculator():
    while True:
        print("\nSimple Calculator")
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        match choice:
            case '1':
                print(f"Result: {num1 + num2}")
            case '2':
                print(f"Result: {num1 - num2}")
            case '3':
                print(f"Result: {num1 * num2}")
            case '4':
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Error: Division by zero!")
            case _:
                print("Invalid choice! Please enter a number between 1 and 5.")
