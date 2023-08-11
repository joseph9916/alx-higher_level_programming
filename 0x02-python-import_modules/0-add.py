#!/usr/bin/env python3
if __name__ == "__main__":
    a = 1
    b = 2
    add_two = __import__('add_0').add

    print("{:d} + {:d} = {:d}".format(a, b, add_two(a, b)))
