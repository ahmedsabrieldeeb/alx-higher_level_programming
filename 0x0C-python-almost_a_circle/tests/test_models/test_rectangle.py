#!/usr/bin/python3
"""A test case for rectangle class"""


import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """A test class to test rectangle class"""

    def test_init(self):
        """Test cases of class objects"""
        self.rect_1 = Rectangle(10, 2)
        self.assertEqual(self.rect_1.id, 1)

        self.rect_2 = Rectangle(10, 2)
        self.assertEqual(self.rect_2.id, 2)

        self.rect_3 = Rectangle(10, 2, 0, 0, 15)
        self.assertEqual(self.rect_3.id, 15)

        self.rect_4 = Rectangle(10, 2)
        self.assertEqual(self.rect_4.width, 10)

        self.rect_5 = Rectangle(10, 2)
        self.assertEqual(self.rect_5.height, 2)

        self.rect_6 = Rectangle(10, 2, 6)
        self.assertEqual(self.rect_6.x, 6)

        self.rect_7 = Rectangle(10, 2, 0, 0, 100)
        self.assertEqual(self.rect_7.id, 100)

if __name__ == '__main__':
    unittest.main()
