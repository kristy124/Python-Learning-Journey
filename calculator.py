def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

from calcArt import logo

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    continue_calc = True

    while continue_calc:
        operation_symbol = input("Pick an operation: ")
        while operation_symbol not in operations:
            print('Please type a valid operation')
            operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        should_continue = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation: ")
        if should_continue == 'y':
            num1 = answer
        elif should_continue == 'n':
            continue_calc = False
            calculator()
        else:
            while should_continue != 'y' and should_continue != 'n':
                print('Please type a valid response.')
                should_continue = input(f"Type 'y' to continue calculating with {answer}, type 'n' to exit.: ")
                num1 = answer


calculator()