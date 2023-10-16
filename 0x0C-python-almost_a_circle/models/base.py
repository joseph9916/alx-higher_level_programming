#!/usr/bin/python3
"""
Write the first class Base:
"""


import json
import os
import csv


class Base:
    """
    Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        if id is not None, assign the public instance attribute id with this
        argument value
        otherwise, increment __nb_objects and assign the new value to the
        public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file:
        """
        list_dictionaries = []
        for obj in list_objs:
            list_dictionaries.append(obj.to_dictionary())
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set:
        """
        obj = cls(1, 2)
        obj.update(**dictionary)
        return obj
    
    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances:
        """
        filename = "{}.json".format(cls.__name__)
        list_obj = []
        if os.path.isfile(filename):
            with open(filename, 'r', encoding="utf-8") as f:
                json_string = f.read()
                list_dictionaries = cls.from_json_string(json_string)
                for dictionary in list_dictionaries:
                    list_obj.append(cls.create(**dictionary))
        return list_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        that serializes in CSV
        """
        list_dictionaries = []
        for obj in list_objs:
            list_dictionaries.append(obj.to_dictionary())
        filename = "{}.csv".format(cls.__name__)
        if cls == Rectangle.__name__:
            fields = ["id", "width", "height", "x", "y"]
        if cls == Square.__name__:
            fields = ["id", "size", "x", "y"]

        with open(filename, 'w', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for row in list_dictionaries:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """
        that deserializes in csv
        """
        list_objs = []
        filename = "{}.csv".format(cls.__name__)
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj = cls.create(row)
                list_objs.append(obj)
        return list_objs


class Rectangle(Base):
    """Dummy Rectangle class"""
    def __init__(self, width=1, height=1, x=0, y=0, id=None):
        """Dummy instance"""
        pass

class Square(Rectangle):
    """Dummy Square class"""
    def __init__(self, size=1, x=0, y=0, id=None):
        """Dummy Square instance"""
        pass
