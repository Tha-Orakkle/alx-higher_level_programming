#!/usr/bin/python3
"""
Module matrix_divided
Divides the element of a matrix by a number
"""


def matrix_divided(matrix, div):
    """Returns a new matrix(list of lists).
    The elements if the matrix will be the result of
    the division of the elements by div and rounded
    to 2 decimal places.
    """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) != list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    length = len(matrix[0])

    for row in matrix:
        if type(row) != list or len(row) == 0 or length == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    new_matrix = [[round(col / div, 2) for col in row] for row in matrix]

    return new_matrix
