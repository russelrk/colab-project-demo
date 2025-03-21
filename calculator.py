
from src.add.add import add
from src.subtract.subtract import subtract
from src.multiply.multiply import multiply
from src.divide.divide import divide

def calculator():
    print("Simple Modular Calculator")
    print("Options: +  -  *  /")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        else:
            result = "Invalid operator"

        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
if __name__ == "__main__":
    calculator()
