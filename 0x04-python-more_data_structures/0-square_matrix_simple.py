#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list()
    for i in range(len(matrix)):
        row = list()
        for j in range(len(matrix[i])):
            row.append(matrix[i][j] ** 2)
        new_matrix.append(row)
    return new_matrix
