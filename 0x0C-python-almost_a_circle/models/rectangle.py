#!/usr/bin/python3
"""A class inherits from another class"""


from models.base import Base


class Rectangle(Base):
    """A Recntangle class inheriting from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        A constructor to initialize class objects

        Args:
            width (int): width of recatangle
            height (int): height of rectangle
            x (int): x-coordinate
            y (int): y-coordinate
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """overwrite __str__ method to print custom output"""
        return f"""\
[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}\
"""

    @property
    def width(self):
        """Get width of Rectangle bject"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set width of Rectangle object

        Args:
            value (int): value set to width

        Raises:
            TypeError: width must be an int
            ValueError: width must be > 0
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if (value <= 0):
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Get height of Rectangle bject"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set height of Rectangle object

        Args:
            value (int): value set to height

        Raises:
            TypeError: height must be an int
            ValueError: height must be > 0
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if (value <= 0):
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Get x of Rectangle object"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set x-coordinate of Rectangle object

        Args:
            value (int): value set to x-coordinate

        Raises:
            TypeError: x must be an int
            ValueError: x must be >= 0
        """
        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if (value < 0):
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Get y of Rectangle object"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set y-coordinate of Rectangle object

        Args:
            value (int): value set to y-coordinate

        Raises:
            TypeError: y must be an int
            ValueError: y must be >= 0
        """
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if (value < 0):
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Returning rectangle area"""
        return self.__height * self.__width

    def display(self):
        """Printing the Rectangle with # symbols"""
        for ys in range(self.__y):
            print()

        for rows in range(self.__height):
            for xs in range(self.__x):
                print(' ', end='')
            for cols in range(self.__width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """
        update attributes of the object

        Args:
            args (list): variable non-keyworded list of args
            kwargs (dict): varibale keyworded dictionary of args

        Notes on args:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute

        Notes on kwargs:
            **kwargs must be skipped if *args exists and is not empty
            Each key in this dictionary represents an attribute to the instance
        """
        attribute_mapping = {
            'id':     'self.id=',
            'width':  'self.width=',
            'height': 'self.height=',
            'x':      'self.x=',
            'y':      'self.y='
        }

        if args:
            for idx, arg in enumerate(args):
                attribute_name = list(attribute_mapping.keys())[idx]
                exec(attribute_mapping[attribute_name] + str('arg'))
        else:
            for key, value in kwargs.items():
                if key in attribute_mapping:
                    exec(attribute_mapping[key] + str('value'))

    def to_dictionary(self):
        """Returning dictionary representation of the object"""
        return {
            'id':     self.id,
            'width':  self.width,
            'height': self.height,
            'x':      self.x,
            'y':      self.y
        }
