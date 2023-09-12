#!/usr/bin/python3
import json
"""
Write a function that writes an Object to a text file,
using a JSON representation:
"""


def save_to_json_file(my_obj, filename):
    """
    Encodes a python object to JSON string and writes into a text file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
