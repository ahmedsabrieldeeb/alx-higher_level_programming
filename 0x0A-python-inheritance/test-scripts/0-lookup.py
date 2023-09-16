#!/usr/bin/python3
"""
A module having one function
"""


def lookup(obj):
    """
    A function that returns the list of available
    attributes and methods of an object

    Args:
        obj (any obj): any king of object

    Returns:
        list: a list of attrs and methods
    """
    return dir(obj)
