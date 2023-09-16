#!/usr/bin/python3
"""A module having one class implemented inherting from another"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry with more methods"""

    def __init__(self, width, height):
        """
        Constructor to set rectangle's width and height
        Without getter and setter

        Args:

            width (int): width of rectangle
            height (int): height of rectangle
        """

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Overwrite the area method (originally defined in BaseGeometry() class)
        implementing its function

        Returns:
            int: area of rectangle object
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Overwire the __str__ method to return a specific statement

        Returns:
            str: text to be used as represnting the object (not __repr__)
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
