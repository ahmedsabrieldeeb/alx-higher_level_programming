#!/usr/bin/python3
"""A module having one class"""


class BaseGeometry():
    """A class that checks for values passed"""

    def area(self):
        """
        An empty function raising an error since it is empty
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validating value (second argument) passed

        Args:
            name (str): name is always string
            value (don't know): the argument that should be int

        Raises:
            TypeError: when value is not an integer
            ValueError: when value is not greater than zero
        """
        if (type(value) != int):
            raise TypeError(f"{name} must be an integer")

        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
