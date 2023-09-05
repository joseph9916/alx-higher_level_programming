#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, (float, int)) or not isinstance(b, (float, int)):
        raise TypeError("a must be an integer or b must be an integer")
    if a is None:
        raise TypeError("a must be an integer or b must be an integer")
    a = int(a)
    b = int(b)
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.textfile("./tests/0-add_integer.txt")
