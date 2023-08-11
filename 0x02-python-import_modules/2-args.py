#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("{:d} arguement".format(len(sys.argv) - 1))
    else:
        print("{:d} arguements".format(len(sys.argv) - 1)) 
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
