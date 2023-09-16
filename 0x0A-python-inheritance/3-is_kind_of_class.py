#!/usr/bin/python3
"""A module having one function"""


def is_kind_of_class(obj, a_class):
    """
    Is obj (first argument) generally
    an instance of the a_class (second argument)
    
    Returns:
        True if yes, False if no
    """
    return isinstance(obj, a_class)
