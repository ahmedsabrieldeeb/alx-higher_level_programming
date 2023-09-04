#!/usr/bin/python3

"""
    A module that cotains only one function
    a function that prints your full name.
"""


def say_my_name(first_name, last_name=""):
    """
    A function to print: My name is <first name> <last name>

    Args:
        first_name (string): the first name.
        last_name (string):  the last name.
        Defaults to empty string if not provided.

    Returns:
        No returns

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
