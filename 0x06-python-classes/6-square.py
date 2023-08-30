#!/usr/bin/python3
"""A class to define a Square."""


class Square:
    """Defining a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            self: argument referring to object calling the method.
            size (int): size of square to be set initializingly.
            position (tuple): tuple of two intergers as coordinated
            to print the square with
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        getting the value of size of the square.
        Args:
            self: argument referring to object calling the method.
        """
        return self.__size

    @property
    def position(self):
        """
        getting the value of position of the square.
        Args:
            self: argument referring to object calling the method.
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        Args:
            self: argument referring to object calling the method.
            value (int): value to which the __size is set
        """
        if (
            not isinstance(value, tuple)
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or len(value) != 2
            or value[0] < 0 or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        if (self.__size == 0):
            print()
            return

        for ys in range(self.__position[1]):
            print()

        for rows in range(self.__size):
            for xs in range(self.__position[0]):
                print(" ", end='')
            for cols in range(self.__size):
                print("#", end='')
            print()
