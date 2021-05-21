#!/usr/bin/python3
"""
This module contains a function matrix_divided that divides all elemnts of a
matrix by an integer or a float identified as div
"""


def matrix_divided(matrix, div):
    """ Returns a new matrix that consists of all the elements in the argument
    matrix divided by div.
    if if it fails it raises errors.
    """

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of integers/floats")

    #find length of rows and save to compare
    row_lengths = []
    for row in matrix:
        row_lengths.append(len(row))
    if len(set(row_lengths)) is not 1:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2)for x in row] for row in matrix]

    return new_matrix
