#!/usr/bin/python3
import json
"""
Write a function that creates an Object from a JSON file
"""


def load_from_json_file(filename):
    """
    Decodes a JSON file and creates an object
    """
    with open(filename, 'r', encoding="utf-8") as f:
        my_obj = json.load(f)
    return my_obj
