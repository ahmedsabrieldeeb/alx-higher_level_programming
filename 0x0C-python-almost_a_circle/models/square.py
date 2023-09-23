#!/usr/bin/python3
"""A Square class inheriting from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructor for Square class

        Args:
            size (int): square side length
            x (int): x-coordinate
            y (int): y-coordinate
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overwrite __str__ method to print custom output"""
        return f"""\
[Square] ({self.id}) {self.x}/{self.y} - {self.size}\
"""

    @property
    def size(self):
        """Get size of square object"""
        return self.__width

    @size.setter
    def size(self, value):
        """
        Set size of square object with parent class setter

        Args:
            value (int): value to be assigned
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if (value <= 0):
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value
