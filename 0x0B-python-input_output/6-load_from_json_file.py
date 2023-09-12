#!/usr/bin/python3
"""
Module of seventh task
"""


import json


def load_from_json_file(filename):
    """
    Load JSON file

    Args:
        filename (str): the file name of JSON file

    Returns:
        corresponding python object(s)
    """
    with open(filename, "r", encoding="utf-8") as f:
        return (json.load(f))
