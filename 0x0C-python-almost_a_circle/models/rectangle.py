#!/usr/bin/python3
"""
Write the class Rectangle that inherits from Base
"""


import models.base as base


class Rectangle(base.Base):
    """A Rectangle class that inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Call the super class with id - this super call with
        use the logic of the __init__ of the Base class
        Assign each argument width, height, x and y to the right attribute
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width"""
        self.integer_validation(value, "width")
        self.__width = value

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for width"""
        self.integer_validation(value, "height")
        self.__height = value

    @property
    def x(self):
        """getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for x"""
        self.integer_validation(value, "x")
        self.__x = value

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for width"""
        self.integer_validation(value, "y")
        self.__y = value

    def integer_validation(self, value, name):
        """validate value as integer for width and height"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if name == "height" or name == "width":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Calculate area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """prints an unofficial representation of rectangle"""
        str = ("[Rectangle] ({}) {}/{} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height))
        return str

    def display(self):
        """to print in stdout the Rectangle instance with the character
        # by taking care of x and y"""
        str = ""
        str += "\n" * self.y
        for i in range(self.__height):
            str += (" " * self.x + "#" * self.width + "\n")
        print(str, end="")

    def update(self, *args, **kwargs):
        """Update the class Rectangle by adding the public method
        def update(self, *args): that assigns an argument to each attribute:
        or  that assigns a key/value argument to attributes:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        if len(args) != 0:
            self.id = args[0]
            if len(args) > 1:
                self.x = args[1]
            if len(args) > 2:
                self.y = args[2]
            if len(args) > 3:
                self.width = args[3]
            if len(args) > 4:
                self.height = args[4]
        else:
            if id in kwargs:
                self.id = kwargs.get("id", self.id)
            if "x" in kwargs:
                self.x = kwargs.get("x")
            if "y" in kwargs:
                self.y = kwargs.get("y")
            if "width" in kwargs:
                self.width = kwargs.get("width")
            if "height" in kwargs:
                self.height = kwargs.get("height")

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        rect_dict = ({'x': self.x, 'y': self.y, 'id': self.id,
            'height': self.height, 'width': self.width})
        return rect_dict
