#!/usr/bin/python3
"""A module having one function"""


def is_same_class(obj, a_class):
    """
    Is obj (first argument) exactly
    an instance of the a_class (second argument)

    Returns:
        True if yes, False if no
    """
    return (type(obj) == a_class)
