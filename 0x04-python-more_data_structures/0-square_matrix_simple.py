#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [num**2 for row in matrix for num in row]
    return new_matrix
