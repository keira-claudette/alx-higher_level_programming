#!/usr/bin/python3
""" Module: rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiation"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """ A getter for width"""
            return self.__width

        @width.setter
        def width(self, value):
            """Sets width to value"""
            self.__width = value

        @property
        def height(self):
            """ A getter for height"""
            return self.__height

        @height.setter
        def height(self, value):
            """Sets height to value"""
            self.__height = value

        @property
        def x(self):
            """ A getter for x"""
            return self.__x

        @x.setter
        def x(self, value):
            """Sets x to value"""
            self.__x = value

        @property
        def y(self):
            """ A getter for y"""
            return self.__y

        @y.setter
        def y(self, value):
            """Sets y to value"""
            self.__y = value
