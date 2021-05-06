#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    power_2 = lambda x : x **2
    for i in matrix:
        squares = []
        squares.append([list(map(power_2, i))])

    return squares
