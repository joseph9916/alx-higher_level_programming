#!/usr/bin/python3
"""
A module of two integer addition with tests
"""


def add_integer(a, b=98):
    """a function to add two integers"""
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    if a is None:
        raise TypeError("a must be an integer")

    a = int(a)
    b = int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.textfile("./tests/0-add_integer.txt")
