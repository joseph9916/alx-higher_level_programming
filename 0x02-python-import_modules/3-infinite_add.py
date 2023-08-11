#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = 0
    if len(sys.argv) == 1:
        print("{:d}".format(result))
    else:
        for i in range(1, len(sys.argv)):
            result += int(sys.argv[i])
        print("{:d}".format(result))
