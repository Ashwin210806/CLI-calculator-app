def show_menu():
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Start of the program
print("Welcome to the Easy Calculator!")

# Repeat until the user exits
while True:
    show_menu()
    choice = input("Choose 1-5: ")

    if choice == '1':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a + b)

    elif choice == '2':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a - b)

    elif choice == '3':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a * b)

    elif choice == '4':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("Result:", a / b)

    elif choice == '5':
        print("Thanks for using the calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose from 1 to 5.")