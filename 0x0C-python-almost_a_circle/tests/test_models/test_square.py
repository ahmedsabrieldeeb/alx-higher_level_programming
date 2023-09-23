#!/usr/bin/python3
"""A test case for squareangle class"""


import unittest
import sys
from io import StringIO

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

    def test_init_wrong(self):
        with self.assertRaises(TypeError):
            Square("1")
        
        with self.assertRaises(TypeError):
            Square(2, "1")

        with self.assertRaises(TypeError):
            Square(5, 6, "1")

        with self.assertRaises(ValueError):
            Square(1, -1)

        with self.assertRaises(ValueError):
            Square(5, 6, -1)

        with self.assertRaises(ValueError):
            Square(-1)

        with self.assertRaises(ValueError):
            Square(0)

    def test_set_size(self):
        sqaure = Square(15, 14, 2, 3)
        self.assertEqual(sqaure.size, 15)
        self.assertEqual(sqaure.width, 15)
        self.assertEqual(sqaure.height, 15)

        sqaure.size = 10
        self.assertEqual(sqaure.size, 10)
        self.assertEqual(sqaure.width, 10)
        self.assertEqual(sqaure.height, 10)

        sqaure.size = 12
        self.assertEqual(sqaure.size, 12)
        self.assertEqual(sqaure.width, 12)
        self.assertEqual(sqaure.height, 12)


    def test_size_type(self):
        sqaure = Square(15)
        self.assertEqual(sqaure.size, 15)

        with self.assertRaises(TypeError):
            sqaure.size = "ahmed"
        
        with self.assertRaises(TypeError):
            sqaure.size = [15, 6]

        with self.assertRaises(TypeError):
            sqaure.size = (14, )

        with self.assertRaises(TypeError):
            sqaure.size = {14, 6}

        with self.assertRaises(TypeError):
            sqaure.size = {'ahmed':15}

    def test_size_value(self):
        square = Square(14)
        self.assertEqual(square.size, 14)

        with self.assertRaises(ValueError):
            square.size = -14
        
        with self.assertRaises(ValueError):
            square.size = 0

    def test_update_args(self):
        square = Square(10, 10, 10, 10)

        square.update(6, 2, 3, 4)
        self.assertEqual(square.id, 6)
        self.assertEqual(square.width, 2)
        self.assertEqual(square.height, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

        square.update(10, 10)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

        with self.assertRaises(TypeError):
            square.update(1, 'ahmed')

        with self.assertRaises(ValueError):
            square.update(1, 5, -9)

    def test_update_kwargs(self):
        square = Square(10, 10)

        square.update(id=15)
        self.assertEqual(square.id, 15)

        square.update(width=300)
        self.assertEqual(square.width, 300)
        
        square.update(x=1, height=2, y=3, width=4)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.height, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.width, 4)

        with self.assertRaises(TypeError):
            square.update(x=5, width="ahmed")
        
        with self.assertRaises(ValueError):
            square.update(x = -6)

        with self.assertRaises(ValueError):
            square.update(size = -6)

    def test_update_args_kwargs(self):
        square = Square(10, 10)

        square.update(10, 20, 30, id=1, width=2, height=3)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.width, 20)
        self.assertEqual(square.height, 20)
        self.assertEqual(square.x, 30)
        self.assertEqual(square.y, 0)

        square.update(14, x=20)
        self.assertEqual(square.id, 14)
        self.assertEqual(square.width, 20)
        self.assertEqual(square.height, 20)
        self.assertEqual(square.x, 30)
        self.assertEqual(square.y, 0)



if __name__ == '__main__':
    unittest.main()
