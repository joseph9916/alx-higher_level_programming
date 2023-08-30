#!/usr/bin/python3
"""
An empty class Square that defines a square with a
Private instance attribute: size
"""


class Square:
    """Instantiation with size"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (len(position) != 2 or (not isinstance(position[1], int))
                or (not isinstance(position[1], int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    """that prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print("{}".format("\n" * (self.__position[0] - 1)))
            for i in range(self.__size):
                print(("{}{}".
                    format(" " * self.__position[0], "#" * self.__size)))

    """Retrieve position"""
    @property
    def position(self):
        return self.__position

    """set position"""
    @position.setter
    def postion(self, value):
        if (len(value) != 2 or not isinstance(value[0], int)
                or not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
