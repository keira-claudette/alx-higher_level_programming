#!/usr/bin/python3
"""
Module: 7-base_geometry

describes an empty class BaseGeometry
"""


class BaseGeometry:
    """ An empty class"""

    def area(self):
        """ Raises exception error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value"""
        if type(value) is int:
            if value <= 0:
                raise ValueError("<name> must be greater than 0")
        else:
            raise TypeError("<name> must be an integer")
