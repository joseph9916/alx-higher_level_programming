#!/usr/bin/python3
"""
Write an empty class BaseGeometry
"""


class BaseGeometry:
    """A base geometry class"""

    def area(self):
        """area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """A Rectangle class inheriting Geometry"""

    def __init__(self, width, height):
        """Initialise rectangle class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area method for rectangle class"""
        return self.__width * self.__height

    def __str__(self):
        """Unofficial string representation of Rectangle class"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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
