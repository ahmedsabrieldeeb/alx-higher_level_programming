#!/usr/bin/python3
"""
Module of second task
"""


def write_file(filename="", text=""):
    """
    write a text to a file in python

    Args:
        filename (str): filename or path
        text (str): the content to be written

    Returns:
        int: number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
