#!/usr/bin/python3
"""
Module of sixth task
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Save JSON file

    Args:
        my_obj: object to be serialized
        filename (str): the file name of JSON file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
