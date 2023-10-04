#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer())
print(add_integer(4, "School"))
try:
    print(add_integer(None))
except Exception as e:
    print(e)
