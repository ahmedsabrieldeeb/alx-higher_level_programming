#!/usr/bin/python3
"""A class to define a Square."""


class Square:
    """Defining a square."""

    __size = 0

    def __init__(self, size):
        """
        Args:
            self: argument referring to object calling the method.
            size: size of square
        """

        self.__size = size
