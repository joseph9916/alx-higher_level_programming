#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = 3
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if size != 0:
            self.__size = size

    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        self.__size = value
        return self.__size

    def area(self):
        return self.__size ** 2
    
