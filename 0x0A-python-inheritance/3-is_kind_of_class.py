#!/usr/bin/python3
"""
Module: 3-is_kind_of_class

Verifies if a given object is an instance of a class or
an inherited class
"""


def is_kind_of_class(obj, a_class):
    """ Returns True if the object is an instance of, or if the
    object is an instance of a class that inherited from,
    the specified class ; otherwise False.

    Arguments: obj - object to check if it's exactly an instance of
    the class or an instance of an inherited class.

    a_class - class to check

    """

    return isinstance(obj, a_class)
