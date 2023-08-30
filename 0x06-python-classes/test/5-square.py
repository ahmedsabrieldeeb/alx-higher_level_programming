#!/usr/bin/python3
"""A class to define a Square."""


class Square:
    """Defining a square."""

    def __init__(self, size=0):
        """
        Args:
            self: argument referring to object calling the method.
            size (int): size of square to be set initializingly.
        """
        self.x = size
        self.size = size

    @property
    def size(self):
        """
        Args:
            self: argument referring to object calling the method.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Args:
            self: argument referring to object calling the method.
            value (int): value to which the __size is set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Args:
            self: argument referring to object calling the method.
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        printing a square using '#' symbols

        Args:
            self: argument referring to object calling the method.
            value (int): value to which the __size is set
        """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
