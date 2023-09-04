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
