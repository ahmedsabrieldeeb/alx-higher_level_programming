#!/usr/bin/python3
"""A test case for base class"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """A test class to test base class"""

    def test_init(self):
        """Test cases of class objects"""
        self.base_1 = Base()
        self.assertEqual(self.base_1.id, 1)

        self.base_2 = Base()
        self.assertEqual(self.base_2.id, 2)

        self.base_3 = Base()
        self.assertEqual(self.base_3.id, 3)

        self.base_4 = Base(15)
        self.assertEqual(self.base_4.id, 15)

        self.base_5 = Base()
        self.assertEqual(self.base_5.id, 4)

if __name__ == '__main__':
    unittest.main()
