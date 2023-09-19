#!usr/bin/python3
"""
Write the class Square that inherits from Rectangle:
In the file models/square.py
"""


import models.rectangle as rectangle


class Square(rectangle.Rectangle):
    """Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Call the super class with id, x, y, width and height -
        this super call will use the logic of the __init__ of the
        Rectangle class. The width and height must be assigned to
        the value of size"""
        width = size
        height = size
        super().__init__(x=x, y=y, width=width, height=height, id=id)

    def __str__(self):
        """overloading __str__ method from rectangle"""
        str = "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
        return str

    @property
    def size(self):
        """getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """*args is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute"""
        if len(args) != 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs.get("id", self.id)
            if "x" in kwargs:
                self.x = kwargs.get("x")
            if "y" in kwargs:
                self.y = kwargs.get("y")
            if "size" in kwargs:
                self.width = kwargs.get("size")
                self.height = self.width

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        square_dict = ({'x': self.x, 'y': self.y, 'id': self.id,
                        'size': self.size})
        return square_dict
