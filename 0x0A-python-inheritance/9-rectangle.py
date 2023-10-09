#!/usr/bin/python3
"""
Write an empty class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class inheriting Geometry"""

    def __init__(self, width, height):
        """Initialise rectangle class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns an unofficial representation of rectangle"""
        string = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return string
