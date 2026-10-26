from calculator_functions import operators

def main():
    while True:
        operator = input("Enter an operator of '+', '-', '*', '/', or 'q' to exit the program: ")
        if operator == 'q':
            print('Goodbye!')
            break
        if operator not in operators:
            print('Please enter a valid operator')
            continue
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print('Please enter a valid number')
                continue

            result = operators[operator](num1, num2)
            print('Result:', result)
            break


if __name__ == '__main__':
    main()