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
