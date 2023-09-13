#!/usr/bin/python3
"""
Module of ninth task
"""


def class_to_json(obj):
    """
    function that returns the dictionary description with simple data structure
    such as (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj: python object

    Returns:
        corresponding object __dict__ attribute
    """
    return (obj.__dict__)
