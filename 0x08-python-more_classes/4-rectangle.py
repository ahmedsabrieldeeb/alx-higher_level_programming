#!/usr/bin/python3

"""
A module contains one class called 'Rectangle'
"""


class Rectangle:
    """
    A class that creates rectangles based on width and height

    Attributes:
        width (int): the width of rectangle
        height (int): the height of rectangle
    """

    def __init__(self, width=0, height=0):
        """
        construct the class with its paramaters
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        A magic __str__ to print a ractangle with '#'
        """
        if self.__height == 0 or self.__width == 0:
            return ""

        row_str = ""
        for rows in range(self.__height):
            for cols in range(self.__width):
                row_str = row_str + '#'
            row_str = row_str + '\n'

        return row_str[:-1]

    def __repr__(self):
        """
        A magic __repr__ to recreate the object for eval purposes
        """

        return f"Rectangle({self.__width}, {self.__height})"

    @property
    def width(self):
        """
        Get the value of width

        Returns:
            int: the value of width
        """
        return self.__width

    @property
    def height(self):
        """
        Get the value of height

        Returns:
            int: the value of height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Set the width to value passed

        Args:
            value (int): the value to be setted

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """
        Set the height to value passed

        Args:
            value (int): the value to be setted

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Returning the area of rectangle

        Returns:
            int: the area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returning the perimeter of rectangle

        Returns:
            int: the perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2
