# Simple Calculator

This is a simple calculator application that runs in the terminal. It supports basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

- Addition
- Subtraction
- Multiplication
- Division

## Usage

1. Clone the repository or copy the `calculator.py` file to your local machine.
2. Open a terminal and navigate to the directory containing the `calculator.py` file.
3. Run the calculator by executing the following command:

    ```bash
    python calculator.py
    ```

4. Follow the prompts to perform calculations by entering expressions in the format `select-operation-choice, num1, num2`.
5. To exit the calculator, type `quit` and press Enter.

## Example

```bash
$ python calculator.py
Simple Calculator
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
Enter choice (1/2/3/4): 1
Enter first number: 3
Enter second number: 4
3.0 + 4.0 = 7.0
Do you want to perform another calculation? (yes/no): yes
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
Enter choice (1/2/3/4): 4
Enter first number: 10
Enter second number: 0
10.0 / 0.0 = Error! Division by zero.
Do you want to perform another calculation? (yes/no): no
Thank you for using the calculator!
```
## Notes

The calculator handles basic error checking for invalid numeric inputs and division by zero.
It supports continuous calculations until the user decides to exit.


This README provides an overview of the calculator application, usage instructions, an example of how to use it, and notes about its features and modifications. 
