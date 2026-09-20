print("Simple Calculator")
print("1. Add  2. Subtract  3. Multiply  4. Divide")

while True:
    choice = input("\nEnter choice (1/2/3/4) or 'q' to quit: ")

    if choice == 'q':
        print("Goodbye!")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == '1':
            print(f"Result: {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("Error! Cannot divide by zero.")
            else:
                print(f"Result: {num1 / num2}")
    else:
        print("Invalid choice! Choose 1, 2, 3, or 4.")