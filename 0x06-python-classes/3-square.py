#!/usr/bin/python3
"""A class to define a Square."""


class Square:
    """Defining a square."""

    __size = 0

    def __init__(self, size=0):
        """
        Args:
            self: argument referring to object calling the method.
            size (int): size of square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Args:
            self: argument referring to object calling the method.
        """
        return (self.__size ** 2)
