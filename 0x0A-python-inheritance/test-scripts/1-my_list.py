#!/usr/bin/python3
"""
A module having one function
"""


class MyList(list):
    """A class that inherits from list with sorting method added"""

    def print_sorted(self):
        """
        Public instance method that prints the list, but ascendingly sorted
        """
        print(sorted(self))
