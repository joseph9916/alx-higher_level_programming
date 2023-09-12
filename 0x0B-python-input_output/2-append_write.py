#!/usr/bin/python3
"""
Write a function that appends a string to a text file (UTF8)
and returns the number of characters written:
"""


def append_write(filename="", text=""):
    """
    a function that appends a string
    function should create the file if doesn’t exist.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        char_written = f.write(text)
    return char_written
