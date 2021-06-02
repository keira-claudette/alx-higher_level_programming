#!/usr/bin/python3
"""
Module: 2-is-same_class
defines a function that checksif object is exactly an instance
 of a specified class
"""


def is_same_class(obj, a_class):
    """ Returns True if the object is exactly an instance
    of the specified class ; otherwise False.

    Arguments: obj - object to compare
    a_class - class to check if object is an instance

    """

    return True if type(obj) is a_class else False
