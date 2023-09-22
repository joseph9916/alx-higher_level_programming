#!/usr/bin/python3
"""
The base class for all other classes
"""


import json


class Base:
    """Base class for other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialise class"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        list_dictionaries = []
        for obj in list_objs:
            list_dictionaries.append(obj.to_dictionary())
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                file.write(cls.to_json_string(list_dictionaries))

    @classmethod
    def create(cls, **dictionary):
        """class method returns an instance with all attributes already set"""
        ins = cls(1, 1, 0, 0)
        ins.update(**dictionary)
        return ins

    @staticmethod
    def from_json_string(json_string):
        """static method that returns the list of the JSON string
        representation"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """class method that returns a list of instances:"""
        filename = cls.__name__ + ".json"
        with open(filename, "r", encoding="utf-8") as file:
            if file is None:
                list_dictionaries = []
            list_dictionaries = cls.from_json_string(file.read()) 
            list_obj = []
            if file is not None:
                for dictionary in list_dictionaries:
                    list_obj.append(cls.create(**dictionary))
        return list_obj

class Rectangle(Base):
    """Dummy Rectangle class"""
    def __init__(self, width=1, height=1, x=0, y=0, id=None):
        """Dummy instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id=id)

class Square(Rectangle):
    """Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Dummy Instance"""
        width = size
        height = size
        super().__init__(x=x, y=y, width=width, height=height, id=id)
