#!/usr/bin/python3
"""Inheris from baseGeometry"""


class BaseGeometry:
    """
    This is the documentation for the BaseGeometry class.
    """

    def area(self):
        """
        This method raises an exception
        indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates an integer value.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    This is the documentation for the Rectangle class.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle instance with width and height.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
