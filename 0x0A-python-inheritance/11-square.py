#!/usr/bin/python3
"""
Module: 10-square
defines a class Square that inherits from
Rectangle (9-rectangle)
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Inherits from rectangle"""

    def __init__(self, size):
        """ Instatiation with size"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ prints formatted string"""

        return str("[Square]{}/{}".format(self.__size, self.__size))

    def area(self):
        """Computes the area of square and overrites
        any prior area() definition
        """

        return self.__size ** 2
