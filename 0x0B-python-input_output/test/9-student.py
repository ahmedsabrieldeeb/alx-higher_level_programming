#!/usr/bin/python3
"""
Module of tenth task
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

    def to_json(self):
        """
        returning the dictionary description with simple data structure
        such as (list, dictionary, string, integer and boolean)
        for JSON serialization of an object

        Args:
            obj: python object

        Returns:
            corresponding object __dict__ attribute
        """
        return (self.__dict__)
