#!/usr/bin/python3
""" Module: base
This module defines a class
"""


class Base:
    """ defines class named Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiates instance attributes"""

        if id is not None:
            self.id = id
        elif id is None:
            self.__class__.__nb_objects += 1
            self.id = self.__nb_objects
