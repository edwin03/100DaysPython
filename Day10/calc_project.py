from art import logo
import os

def add(n1, n2):
    """This adds two values together."""
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

def pOperators():
    for oper in operators:
        print(oper)
    return input("Pick an operation: " )

def calculate(n1, n2, oper):
    return operators[oper](n1, n2)

def clear_screen():
    # for Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for Mac and Linux (here, os.name is 'posix')
    else:
        _ = os.system('clear')

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

cont = "n"

while cont == "n":
    clear_screen()
    print(logo)
    num1 = float(input("What's the first number?: "))
    operator = pOperators()
    num2 = float(input("What's the next number?: "))
    answer = calculate(num1, num2, operator)

    print(f"{num1} {operator} {num2} = {answer}")

    cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

    while cont == "y":
        operator = pOperators()
        num3 = float(input("What's the next number?: "))
        answer = calculate(answer, num3, operator)
        print(f"{answer} {operator} {num3} = {answer}")
        cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()