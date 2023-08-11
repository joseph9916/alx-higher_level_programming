#!/usr/bin/env python3
if __name__ == "__main__":
    a = 1
    b = 2
    add_ = __import__('add_0').add

    result = add_(1, 2)
    print("{:d} + {:d} = {:d}".format(a, b, result))
