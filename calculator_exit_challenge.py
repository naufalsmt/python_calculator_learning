
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

exit_cal = False

while not exit_cal:
    operator = input("enter an operator '+, -, /, *' or 'q' to quit: ")
    if operator.lower() == "q":
        print("bye")
        break
    if operator not in operation:
        print("invalid operator")
        continue

    while True:
        try:
            first_inp = input("enter first number or 'q' to quit: ")
            if first_inp.lower() == "q":
                exit_cal = True
                break

            num1 = float(first_inp)

            second_inp = input("enter second number or 'q' to quit: ")
            if second_inp.lower() == "q":
                exit_cal = True
                break

            num2 = float(second_inp)

        except ValueError:
            print("Invalid input, please enter valid numbers")
            continue

        result = operation[operator](num1, num2)
        print("result:", result)
        break

    if exit_cal:
        print("bye")
        break