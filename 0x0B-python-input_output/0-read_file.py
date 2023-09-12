#!/usr/bin/python3
"""
Module of first task
"""

def read_file(filename=""):
    """
    Read a file in python

    Args:
        filename (str): filename or path
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end='')
