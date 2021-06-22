#!/usr/bin/python3
"""
This program prints all possible different combinations of two digits.
"""
for i in range(0, 9):
    for j in range(i + 1, 10):
        print("{}{}".format(i, j), end=", ")
