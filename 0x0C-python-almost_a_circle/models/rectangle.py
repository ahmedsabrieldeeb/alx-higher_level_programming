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

	@property
	def width(self):
		"""Get width of Rectangle bject"""
		return self.__width

	@width.setter
	def width(self, value):
		"""Set width of Rectangle object"""
		self.__width = value

	@property
	def height(self):
		"""Get height of Rectangle bject"""
		return self.__height

	@height.setter
	def height(self, value):
		"""Set height of Rectangle object"""
		self.__height = value

	@property
	def x(self):
		"""Get x of Rectangle bject"""
		return self.__x

	@x.setter
	def x(self, value):
		"""Set x of Rectangle object"""
		self.__x = value

	@property
	def y(self):
		"""Get y of Rectangle bject"""
		return self.__y

	@y.setter
	def y(self, value):
		"""Set y of Rectangle object"""
		self.__y = value
