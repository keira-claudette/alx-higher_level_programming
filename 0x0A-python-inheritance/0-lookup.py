#!/usr/bin/python3
"""
module 0-lookup describes a function that
lists available attributes and methods
"""


def lookup(obj):
    """ Returns a list of available attributes and methods.

    Args: obj - an object
    """

    return dir(obj)
