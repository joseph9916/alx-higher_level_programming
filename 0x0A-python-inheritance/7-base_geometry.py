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
        

if __name__ == "__main__":
    import doctest
    doctest.textfile("tests/7-base_geometry.txt")
