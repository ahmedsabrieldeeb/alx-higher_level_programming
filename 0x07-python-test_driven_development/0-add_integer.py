#!/usr/bin/python3

"""
    A module that cotains only one function
    that adds two integers and returns the sum
"""


def add_integer(a, b=89):
    """
    A function to add two integers

    Args:
        a (int or float): the first operand
        b (int or float, optional): the second operand.
                                    Defaults to 10 if not provided.

    Returns:
        int or float: representing the sum of two arguments

    Raises:
        TypeError: a must be integer
        TypeError: b must be integer

    Notes:
        Casting both a and b is happened first
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be integer")

    return int(a) + int(b)

