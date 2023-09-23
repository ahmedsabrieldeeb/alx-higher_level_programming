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
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set size of square object with parent class setter

        Args:
            value (int): value to be assigned
        """
        self.width = value
        self.__size = value

    def update(self, *args, **kwargs):
        """
        update attributes of the object

        Args:
            args (list): variable non-keyworded list of args
            kwargs (dict): varibale keyworded dictionary of args

        Notes on args:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute

        Notes on kwargs:
            **kwargs must be skipped if *args exists and is not empty
            Each key in this dictionary represents an attribute to the instance
        """
        pass
