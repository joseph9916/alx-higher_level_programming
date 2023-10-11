#!/usr/bin/python3
"""
Write a function that writes an Object to a text file,
using a JSON representation:
"""


import json


def load_from_json_file(filename):
    """a function that saves to json"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
