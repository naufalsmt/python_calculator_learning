def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "cannot divide by zero"
    return a / b


def get_num(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number:")


operators = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

while True:
    operator = input('select an operator "+", "-", "*", "/" or "q" to exit program: ')
    if operator.lower() == "q":
        print("Goodbye")
        break

    if operator not in operators:
        print("Invalid operator")
        continue

    num1 = get_num("Enter first number: ")
    num2 = get_num("Enter second number: ")
    result = operators[operator](num1, num2)
    print("Result", result)
