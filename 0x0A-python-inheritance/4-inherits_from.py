#!/usr/bin/python3
"""Module: 4-inherits_from.
Verifies if the object is an instance of a class that inherited
(directly or indirectly) from the specified class."""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a class that
    inherited from a_class.
    Arguments:
        @obj -  object to verify
        @a_class -  class to evaluate
    Returns: True or False
    """

    return isinstance(obj, a_class) and type(obj) != a_class
