#!/usr/bin/python3
""" Module: 8-rectangle

Defines a class Rectangle that inherits from
 BaseGeometry (module: 7-base_geometry).
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A new class inherited from BaseGeometry"""

    def __init__(self, width, height):
        """ Instamtiation of args: Width and Height define
        rectangle."""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
