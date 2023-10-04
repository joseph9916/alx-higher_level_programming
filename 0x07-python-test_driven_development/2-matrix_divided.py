#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    matrix must be a list of lists of integers or floats,
    Each row of the matrix must be of the same size
    div must be a number (integer or float)
    div can’t be equal to 0
    """
    if not isinstance(matrix, list) or not isinstance(matrix[0], list):
        raise TypeError(("matrix must be a matrix (list of lists)\
        of integers/floats"))
    size = len(matrix[0])
    if not isinstance(div, (int, float)) or not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for num in row:
            num = round((num / div), 2)
            new_row.append(num)
        new_matrix.append(new_row)
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.textfile("tests/2-matrix_divided.txt")
