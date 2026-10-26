
def addition(a,b):
    return a+b


def subtraction(a,b):
    return a-b


def multiplication(a,b):
    return a*b


def division(a,b):
    if b == 0:
        return "cannot divide by zero"
    return a/b

operation = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division
}

while True:
    operator = input("enter an operator '+, -, /, *' or 'q' to quit: ")
    if operator.lower() == "q":
        print("bye")
        break
    if operator not in operation:
        print("invalid operator")
        continue

    while True:
        try:
         num1 = float(input("enter first number: "))
         num2 = float(input("enter second number: "))

        except ValueError:
            print("Invalid input, please enter valid numbers")
            continue

        result = operation[operator](num1, num2)
        print("result:", result)
        break