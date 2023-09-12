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
