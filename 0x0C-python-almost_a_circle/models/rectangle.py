#!/usr/bin/python3
"""
Write the class Rectangle that inherits from Base:
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Call the super class with id
        Assign each argument width, height, x and y to the right attribute
        """
        super().__init__(id)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """witdth setter"""
        self._validate(width, "width")
        self.__width = width
    
    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        self._validate(height, "height")
        self.__height = height

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        self._validate(x, "x")
        self.__x = x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        self._validate(y, "y")
        self.__y = y
    
    def _validate(self, value, name):
        """Validates integer and raises error or nothing if ok"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        print("{}".format("\n" * self.y), end="")
        for row in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def __str__(self):
        """displays an unofficial representation of Rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
            self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """updates Rectangle attributes based on args and kwargs"""
        if args is not None:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        if kwargs is not None:
            self.id = kwargs.get("id", self.id)
            self.width = kwargs.get("width", self.width)
            self.height = kwargs.get("height", self.height)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle:"""
        return ({'x': self.x, 'y': self.y, 'height': self.height,
            'id' : self.id, 'width' :self.width})
