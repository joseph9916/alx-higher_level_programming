#!/usr/bin/python3
"""
Write a function that prints a square with the character #
"""


def print_square(size):
    """
    size is the size length of the square
    size must be an integer, otherwise raise a TypeError
    if size is less than 0, raise a ValueError
    if size is a float and is less than 0, raise a TypeError
    """
    if isinstance(size, (float)) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
    for i in range(size):
        print("{:s}".format("#" * size))
