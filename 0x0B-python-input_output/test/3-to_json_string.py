#!/usr/bin/python3
"""
Module of fourth task
"""


import json


def to_json_string(my_obj):
    """
    Represent the object in JSON

    Args:
        myobj: a python object

    Returns:
        JSON represntation
    """
    return (json.dumps(my_obj))
