#!/usr/bin/python3
"""
Write the class Square that inherits from Rectangle:
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Call the super class with id, x, y, width and height
        """
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """should return [Square] (<id>) <x>/<y> - <size>"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
            self.size))

    def update(self, *args, **kwargs):
        """updates Square attributes based on args and kwargs"""
        if args is not None:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        if kwargs is not None:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("width", self.size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """eturns the dictionary representation of a Rectangle:"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y} 
