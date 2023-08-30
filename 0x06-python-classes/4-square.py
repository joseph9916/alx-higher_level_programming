#!/usr/bin/python3
"""
An empty class Square that defines a square with a
Private instance attribute: size
"""


class Square:
    """Instantiation with size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """get size of square"""
    @property
    def size(self):
        return self.__size

    """set size of square"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    """Calculate Area"""
    def area(self):
        return self.__size ** 2
