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
        if list_dictionaries is not None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write(to_json_string([]))
            else:
                file.write(to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """class method returns an instance with all attributes already set"""
        if cls is Rectangle:
            rect = Rectangle(1, 2)
            rect.update(dictionary)
        if cls is Square:
            square = Square(1)
            square.update(dictionary)

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
        filename = "{}.json".format(cls.__name__)
        with open(filename, "r", encoding="utf-8") as file:
            if file is None:
                list_objs = []
            list_objs = from_json_string(file.read())
            for obj in list_objs:
                cls.create(obj)
