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
            return (json.dumps(list_dictionaries))
        else:
            return ("[]")

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a file

        Args:
            list_objs (list): list of objects
        """

        with open(f"{cls.__name__}.json", "w") as f:
            if not list_objs:
                f.write("[]")
            else:
                list_to_objs = []
                for obj in list_objs:
                    list_to_objs.append(obj.to_dictionary())
                f.write(str(cls.to_json_string(list_to_objs)))

    @staticmethod
    def from_json_string(json_string):
        """
        Represent the object in JSON

        Args:
            json_string: a string coming from JSON

        Returns:
            the original obejct

        Notes:
            If json_string is None or empty, return an empty list
            Otherwise, return the list represented by json_string
        """
        if json_string:
            return (json.loads(json_string))
        else:
            return ([])

    @classmethod
    def create(cls, **dictionary):
        """
        Create an object from a dictionary

        Args:
            dictionary (dict): a dictionary of attributes

        Returns:
            object: an instance of the class
        """
        dummy_obj = cls(7, 13)
        dummy_obj.update(**dictionary)
        return (dummy_obj)
