#!/usr/bin/python3
"""A test case for rectangle class"""


import unittest
import sys
from io import StringIO

from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Test class to Square class"""

    def setUp(self):
        """cleaning up before each test case utilizing name mangling"""
        Base._Base__nb_objects = 0
    
    def test_init_default(self):
        square = Square(14, 2, 3)
        self.assertEqual(square.height, 14)
        self.assertEqual(square.width, 14)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)
        
        square = Square(10)
        self.assertEqual(square.height, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertEqual(square.id, 2)

        square = Square(12, id=15)
        self.assertEqual(square.height, 12)
        self.assertEqual(square.width, 12)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertEqual(square.id, 15)

        square = Square(16, y=5)
        self.assertEqual(square.height, 16)
        self.assertEqual(square.width, 16)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 5)
        self.assertEqual(square.id, 3)


if __name__ == '__main__':
    unittest.main()
