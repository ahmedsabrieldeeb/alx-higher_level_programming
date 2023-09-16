#!/usr/bin/python3
"""A module having one function"""


def inherits_from(obj, a_class):
    """
    Is obj (first argument) inherits from
    the class a_class (second argument) directly or indireclty

    Returns:
        True if yes, False if no
    """
    return isinstance(obj, a_class) and type(obj) != a_class
