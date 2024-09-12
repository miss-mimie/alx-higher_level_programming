#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

def perform_calculation(a: int, b: int ) -> None:
    """
    Performs basic maths operations

    Args:
    a (int): operand 1
    b (int): operand 2

    """

    operators = {"+":add, "-":sub, "*":mul, "/":div}

    for operator, calculator in operators.items():
        print("{} {} {} = {}".format(a, b, calculator(a, b)))


        if __name__ == "__main__":
            a = 10
            b = 5

            perform_calculation(a, b)
