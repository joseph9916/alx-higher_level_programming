#!/usr/bin/python3
"""
Write a function that returns an object (Python data structure)
represented by a JSON string:
"""


import json
def from_json_string(my_obj):
    """
    Decodes a JSON string to a python object
    """
    return json.loads(my_obj)
