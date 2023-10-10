#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal’s triangle of n:
Returns an empty list if n <= 0
You can assume n will be always an integer
"""

def factorial(n):
    """factorial of number"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def pascal_triangle(n):
    """prints the pascal triangle"""
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(factorial(i) // (factorial(j) * factorial(i - j)))
        triangle.append(row)
    return triangle
