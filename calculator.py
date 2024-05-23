# calculator function
def calculator():
    def print_operations():
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

    while True:

         # Print the available operations
        print_operations()

        # Prompt the user to select an operation
        choice = input("Enter choice(1/2/3/4): ")

        # Check if the user input is one of the valid choices
        if choice in ['1', '2', '3', '4']:
            try:
                # Prompt the user to enter two numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                # Handle invalid numeric input
                print("Invalid input. Please enter numeric values.")
                continue

            # Perform the chosen operation and print the result
            if choice == '1':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                result = "Error! Division by zero." if num2 == 0 else num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            # Handle invalid operation choice
            print("Invalid input. Please enter a number between 1 and 4.")

        # Ask if the user wants to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

    print("Thank you for using the calculator!")

# Entry point of the program
if __name__ == "__main__":
    calculator()
