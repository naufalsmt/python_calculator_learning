a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
print("Operator: '+', '-', '*', '/'")
op = input("Select an operator: ")

if op == "+":
    result = a+b
    print("result: ", result)
elif op == "-":
    result = a-b
    print("result: ", result)
elif op == "*":
    result = a*b
    print("result: ", result)
elif op == "/":
    if b != 0:
        result = a/b
        print("result: ", result)
    else:
        print("Cannot devide by zero")
print("Thank you for using this program")