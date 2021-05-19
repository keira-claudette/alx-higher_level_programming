#!/usr/bin/python3
""" This is an empty module"""


class Square:
    """ Defines/represents a square"""
    def __init__(self, size=0):
        """ Initializing the data"""
        self.__size = size

    @property
    def size(self):
        """retrieving the data"""
        return self.__size

    @size.setter
    def size(Self, value):
        """"assigns value to size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square given size"""
        return self.__size ** 2
