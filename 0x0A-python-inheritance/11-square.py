#!/usr/bin/python3
"""
Write an empty class BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class inheriting Rectangle"""

    def __init__(self, size):
        """Initialise Square class"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area of Square"""
        return self.__size ** 2

    def __str__(self):
        """Unofficial string representation of Square class"""
        return "[Square] {}/{}".format(self.__size, self.__size)
