#!/usr/bin/python3

"""
This module provides a function that adds two numbers.
"""


def add_integer(a: "float | int", b: "float | int" = 98) -> int:
    """Returns the sum of two integers.

    Args:
        a (float | int): The first number.
        b (float | int, optional): The second number. Defaults to 98.

    Raises:
        TypeError: When the operands given are not of a valid type (integers).

    Returns:
        int: The sum of the two numbers as an integer.

    Tests:
        >>> add_integer(0)
        98
        >>> add_integer(1, -2)
        -1
        >>> add_integer('1', '67')
        Traceback (most recent call last):
        ...
        TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # ensure the operands are of integer type
    try:
        int(a)
        int(b)
    except Exception as err:
        raise err

    return int(a) + int(b)
