#!/usr/bin/python3
"""A module having two-level inheritance classes"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits from BaseGeometry with more methods"""

    def __init__(self, size):
        """
        Constructor to set rectangle's width and height
        Without getter and setter

        Args:

            size (int): length
        """

        super().integer_validator("size", size)

        self.__size = size

    def area(self):
        """
        Overwrite the area method (originally defined in BaseGeometry() class)
        implementing its function

        Returns:
            int: area of rectangle object
        """
        return self.__size ** 2

    def __str__(self):
        """
        Overwire the __str__ method to return a specific statement

        Returns:
            str: text to be used as represnting the object (not __repr__)
        """
        return f"[ٍSquare] {self.__size}/{self.__size}"
