#!/usr/bin/python3
"""
Module of eleventh task
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

        if attrs == None:
            return self.__dict__
        
        if type(attrs) != list:
            return self.__dict__
    
        for element in attrs:
            if (type(element) != str):
                return self.__dict__
    
        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
