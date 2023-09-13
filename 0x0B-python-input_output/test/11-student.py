#!/usr/bin/python3
"""
Module of twelvth task
"""


class Student:
    """
    Class of Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Args:
            self: argument referring to object calling the method
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returning the dictionary description
        with filter of attrs

        Args:
            self: instance object
            attrs (list): a list of strings (filter)
        Returns:
            corresponding object __dict__ attribute
        """
        my_dict = self.__dict__
        if not attrs:
            return (my_dict)

        my_dict = dict([(key, my_dict[key]) for key in attrs
                        if key in list(my_dict)])
        return (my_dict)

    def reload_from_json(self, json):
        """
        Replaceing all attributes of the Student instance

        Args:
            json (dict): a dictionary of information
        """
        for key in json:
            self.key = json[key]
