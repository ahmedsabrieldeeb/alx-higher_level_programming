#!/usr/bin/python3
"""
Module of fifth task
"""


import json


def from_json_string(my_str):
    """
    Represent the object in JSON

    Args:
        my_str: a string coming from JSON

    Returns:
        the original obejct
    """
    return (json.loads(my_str))
