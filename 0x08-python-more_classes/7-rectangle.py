#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle
"""


class Rectangle:
    """A simple Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Instantiation with optional width and height
        width must be an int
        height must be an int
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def height(self):
        """gets height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height if rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """gets width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets height if rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """calculates area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints an unofficial representation of rectangle"""
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        for i in range(self.__height - 1):
            str += print_symbol * self.__width
            str += "\n"
        str += print_symbol * self.__width
        return str

    def __repr__(self):
        """prints an official representation of rectangle"""
        str = "Rectangle({:d}, {:d})".format(self.__width, self.__height)
        return str

    def __del__(self):
        """Delete a rectangle instance"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
        del (self)
