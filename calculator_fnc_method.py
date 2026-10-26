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


num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
print("operator: '+', '-', '*', '/'")
operator = input("enter operator: ")

operation = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division
}

function = operation.get(operator)

if function:
    print("result: ",function(num1,num2))
else:
    print("Invalid operator")