# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract the second number from the first
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide the first number by the second
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."  # Handle division by zero
    else:
        return x / y

# Main calculator function
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
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
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
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
