#!/usr/bin/python3
""" Module has an empty class Square"""


class Square:
    """ Represents a Square that defines a square by: (based on 1-square.py)
    Private instance attribute: size.
    Instantiation with optional size.
    """
    def __init__(self, size=0):
        """ Initializes the data."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
