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
