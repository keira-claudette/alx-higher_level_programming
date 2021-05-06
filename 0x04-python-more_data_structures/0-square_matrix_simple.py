#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def power_2(x):
        return x ** 2

    squares = []
    for i in matrix:
        squares.append(list(map(power_2, i)))

    return squares
