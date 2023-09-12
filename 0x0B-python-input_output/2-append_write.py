#!/usr/bin/python3
"""
Module of third task
"""


def append_write(filename="", text=""):
    """
    append a text to a file in python at the end

    Args:
        filename (str): filename or path
        text (str): the content to be written

    Returns:
        int: number of characters written
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))
