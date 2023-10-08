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
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overwrite __str__ method to print custom output"""
        return f"""\
[Square] ({self.id}) {self.x}/{self.y} - {self.size}\
"""

    @property
    def size(self):
        """Get value of square size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set value to square size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update attributes of the object

        Args:
            args (list): variable non-keyworded list of args
            kwargs (dict): varibale keyworded dictionary of args

        Notes on args:
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3th argument should be the x attribute
            4th argument should be the y attribute

        Notes on kwargs:
            **kwargs must be skipped if *args exists and is not empty
            Each key in this dictionary represents an attribute to the instance
        """
        if args:
            if len(args) >= 2:
                self.size = args[1]
                modified_args = tuple([args[0], args[1], *args[1:]])
                super().update(*modified_args)
            else:
                super().update(*args)
        else:
            if 'size' in kwargs:
                self.size = kwargs['size']
                kwargs.pop('size')
            super().update(**kwargs)

    def to_dictionary(self):
        """Returning dictionary representation of the object"""
        return {
            'id':     self.id,
            'size':   self.size,
            'x':      self.x,
            'y':      self.y
        }
