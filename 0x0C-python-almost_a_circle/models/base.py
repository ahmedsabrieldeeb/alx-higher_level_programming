#!/usr/bin/python3
"""A base Class to all other classes in this package"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return a json string representation of a list of dictionaries

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            str: json string representation of a list of dictionaries
        """
        if (list_dictionaries):
            return json.dumps(list_dictionaries)
        else:
            return ("[]")
