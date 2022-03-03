from art import logo

def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

operations = {'+':addition, '-':subtraction, '*':multiplication, '/':division}


def calculator():
    print(logo)

    first_number = float(input("What's the first number?\n"))

    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation\n")
        second_number = float(input("What's the next number?\n"))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(first_number, second_number)

        print(f"{first_number} {operation_symbol} {second_number} = {answer}")

        if input(f"Type 'y' to continue calculationg with {answer}, or type 'n' to start a new calculation: \n") == 'y':
            first_number = answer
        else:
            should_continue = False
            calculator()

calculator()
