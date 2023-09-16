#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    matrix must be a list of list else raise TypeError
    Each row of the matrix must be of the same size else raise TypeError
    div must be a number (integer or float), otherwise raise a TypeError
    div can’t be equal to 0
    All elements of the matrix should be divided by div, rounded to
    2 decimal places
    Returns a new matrix
    """

    if len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) "
            "of integers/floats")
    if not isinstance(matrix, list) or not isinstance(matrix[0], list):
        raise TypeError(
                "matrix must be a matrix (list of lists) "
                "of integers/floats")
    for i in range(len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    if div == float('inf'):
        new_matrix = [[0] * len(matrix[0])] * len(matrix)
    for row in matrix:
        new_row = []
        for element in row:
            if not isinstance(element, (float, int)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats"
                    )
            new_element = round((element / div), 2)
            new_row.append(new_element)
        new_matrix.append(new_row)
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.textfile("tests/2-matrix_divided.txt")
