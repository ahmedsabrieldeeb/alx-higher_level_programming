#!/usr/bin/python3
"""A test case for rectangle class"""


import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """A test class to test rectangle class"""

    def setUp(self):
        """cleaning up before each test case utilizing name mangling"""
        Base._Base__nb_objects = 0

    def test_init_default(self):
        """Test passing default number of args"""
        rect = Rectangle(10, 5)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_init_wrong_args_number(self):
        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(10)

        with self.assertRaises(TypeError):
            Rectangle(10, 5, 6, 8, 9, 10)

    def test_rect_is_base(self):
        rect = Rectangle(10, 10)
        self.assertEqual(isinstance(rect, Base), True)

    def test_init_of_base_behaviour(self):
        rect = Rectangle(10, 6)
        self.assertEqual(rect.id, 1)

        rect = Rectangle(10, 6)
        self.assertEqual(rect.id, 2)

        rect = Rectangle(10, 6)
        self.assertEqual(rect.id, 3)

        rect = Rectangle(10, 6, 0, 0, 10)
        self.assertEqual(rect.id, 10)

    def test_access_private(self):
        rect = Rectangle(10, 8)
        with self.assertRaises(AttributeError):
            rect.__width

        with self.assertRaises(AttributeError):
            rect.__height

        with self.assertRaises(AttributeError):
            rect.__x

        with self.assertRaises(AttributeError):
            rect.__y

    def test_width_type(self):
        with self.assertRaises(TypeError):
            Rectangle("5", 6)

        with self.assertRaises(TypeError):
            Rectangle(5.5, 6)

        with self.assertRaises(TypeError):
            Rectangle((15, ), 6)

        with self.assertRaises(TypeError):
            Rectangle([14, ], 6)

        with self.assertRaises(TypeError):
            Rectangle({14, }, 6)

        with self.assertRaises(TypeError):
            Rectangle({"num": 5}, 6)

    def test_width_value(self):
        with self.assertRaises(ValueError):
            Rectangle(-6, 6)

        with self.assertRaises(ValueError):
            Rectangle(0, 6)

    def test_height_type(self):
        with self.assertRaises(TypeError):
            Rectangle(6, "5")

        with self.assertRaises(TypeError):
            Rectangle(6, 5.5)

        with self.assertRaises(TypeError):
            Rectangle(6, (15, ))

        with self.assertRaises(TypeError):
            Rectangle(6, [14, ])

        with self.assertRaises(TypeError):
            Rectangle(6, {14, })

        with self.assertRaises(TypeError):
            Rectangle(6, {"num": 5})

    def test_height_value(self):
        with self.assertRaises(ValueError):
            Rectangle(6, -1)

        with self.assertRaises(ValueError):
            Rectangle(6, 0)

    def test_x_type(self):
        with self.assertRaises(TypeError):
            Rectangle(6, 6, "5")

        with self.assertRaises(TypeError):
            Rectangle(6, 6, 5.5)

        with self.assertRaises(TypeError):
            Rectangle(6, 6, (15, ))

        with self.assertRaises(TypeError):
            Rectangle(6, 6, [14, ])

        with self.assertRaises(TypeError):
            Rectangle(6, 6, {14, })

        with self.assertRaises(TypeError):
            Rectangle(6, 6, {"num": 5})

    def test_x_value(self):
        with self.assertRaises(ValueError):
            Rectangle(6, 6, -6)

    def test_y_type(self):
        with self.assertRaises(TypeError):
            Rectangle(6, 6, 6, "5")

        with self.assertRaises(TypeError):
            Rectangle(6, 6, 6, 5.5)

        with self.assertRaises(TypeError):
            Rectangle(6, 6, 6, (15, ))

        with self.assertRaises(TypeError):
            Rectangle(6, 6, 6, [14, ])

        with self.assertRaises(TypeError):
            Rectangle(6, 6, 6, {14, })

        with self.assertRaises(TypeError):
            Rectangle(6, 6, 6, {"num": 5})

    def test_y_value(self):
        with self.assertRaises(ValueError):
            Rectangle(6, 6, 0, -3)

    def test_area(self):
        rect = Rectangle(10, 6)
        self.assertEqual(rect.area(), 60)

        rect = Rectangle(4, 3)
        self.assertEqual(rect.area(), 12)

        rect = Rectangle(5, 9)
        self.assertEqual(rect.area(), 45)

    def test_display_4x6(self):
        rect = Rectangle(4, 6)
        expected_out = "####\n####\n####\n####\n####\n####\n"
        with StringIO() as temp_out:
            sys.stdout = temp_out
            rect.display()
            self.assertEqual(temp_out.getvalue(), expected_out)

    def test_display_3x3(self):
        rect = Rectangle(3, 3)
        expected_out = "###\n###\n###\n"
        with StringIO() as temp_out:
            sys.stdout = temp_out
            rect.display()
            self.assertEqual(temp_out.getvalue(), expected_out)

    def test_magic_str(self):
        rect = Rectangle(10, 3)
        expexted_out = "[Rectangle] (1) 0/0 - 10/3"
        self.assertEqual(str(expexted_out), expexted_out)

        with StringIO() as temp_out:
            sys.stdout = temp_out
            print(rect)
            self.assertEqual(temp_out.getvalue(), expexted_out + '\n')

        rect = Rectangle(3, 4, 5, 6)
        expexted_out = "[Rectangle] (2) 5/6 - 3/4"
        self.assertEqual(str(expexted_out), expexted_out)

        with StringIO() as temp_out:
            sys.stdout = temp_out
            print(rect)
            self.assertEqual(temp_out.getvalue(), expexted_out + '\n')

        rect = Rectangle(1, 1, 3, 0, 15)
        expexted_out = "[Rectangle] (15) 3/0 - 1/1"
        self.assertEqual(str(expexted_out), expexted_out)

        with StringIO() as temp_out:
            sys.stdout = temp_out
            print(rect)
            self.assertEqual(temp_out.getvalue(), expexted_out + '\n')

        rect = Rectangle(10, 3)
        expexted_out = "[Rectangle] (3) 0/0 - 10/3"
        self.assertEqual(str(expexted_out), expexted_out)

        with StringIO() as temp_out:
            sys.stdout = temp_out
            print(rect)
            self.assertEqual(temp_out.getvalue(), expexted_out + '\n')


if __name__ == '__main__':
    unittest.main()
