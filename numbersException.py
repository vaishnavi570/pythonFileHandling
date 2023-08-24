# Features:
# Addition: Add two numbers.
# Subtraction: Subtract one number from another.
# Multiplication: Multiply two numbers.
# Division: Divide one number by another.
# Exception Handling: Implement try-except blocks to handle potential errors, such as division by zero or invalid input.
import argparse


class NegativeNumberException(Exception):
    pass


def check_for_invalid_data(*args):
    for arg in args:
        if arg is None:
            raise ValueError("One of the argument is None")
        if type(arg) != int:
            raise ValueError("One of the argument is not a number")
        if int(arg) < 0:
            raise NegativeNumberException("Negative values cannot be used")


def addition(a, b):
    check_for_invalid_data(a, b)
    print(a + b)


def subtraction(a, b):
    check_for_invalid_data(a, b)
    if a < b:
        raise ValueError("number1 cannot be less than number2")
    print(a - b)


def multiplication(a, b):
    check_for_invalid_data(a, b)
    print(a * b)


def division(a, b):
    check_for_invalid_data(a, b)
    print(a // b)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='calculator',
        description='runs basic calculations'
    )
    parser.add_argument('operation', choices=['addition', 'subtraction', 'multiplication', 'division'],
                        help="operation_for_calculation")
    parser.add_argument('--number1', type=int, help='number_1')
    parser.add_argument('--number2', type=int, help='number_2')
    args = parser.parse_args()

    if args.operation == 'addition':
        addition(a=args.number1, b=args.number2)
    elif args.operation == 'subtraction':

        try:
            subtraction(a=args.number1, b=args.number2)
        except ValueError:
            print("Subtracting number2 from number1 is not possible, hence swaping values ")
            subtraction(a=args.number2, b=args.number1)
    elif args.operation == 'multiplication':
        multiplication(a=args.number1, b=args.number2)
    elif args.operation == 'division':

        try:
            division(a=args.number1, b=args.number2)
        except ZeroDivisionError:
            print("cannot divide by zero, instead dividing by 1")
            division(a=args.number1, b=1)
        except NegativeNumberException:
            print("Negative numbers given,converting to positive and giving result")
            division(a=abs(args.number1), b=abs(args.number2))
    else:
        raise ValueError("invalid operation")
