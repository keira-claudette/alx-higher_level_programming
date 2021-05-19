#!/usr/bin/python3
class Square:
    """ defines a square """
    def __init__(self, size=0):
        """ initilizing the data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """returns the area of the square given size"""
        return self.__size ** 2
