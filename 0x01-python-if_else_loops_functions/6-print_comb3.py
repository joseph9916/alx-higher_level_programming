#!/usr/bin/python3
for i in range(8):
    for j in range(i + 1, 10):
        print("{:02d}".format((i * 10) + j), end=", ")
print("{:02d}".format(89))
