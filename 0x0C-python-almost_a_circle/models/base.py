#!/usr/bin/python3
"""A base Class to all other classes in this package"""


class Base():
    """A base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        A constructor method for classes' objects

        Args:
            id (int): assume it int, otherwise None by default
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
