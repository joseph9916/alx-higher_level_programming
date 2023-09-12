#!/usr/bin/python3
"""
Write a function that writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
    a function that writes a string
    function should create the file if doesn’t exist.
    function should overwrite the content of the file if it already exists.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        char_written = f.write(text)
    return char_written
