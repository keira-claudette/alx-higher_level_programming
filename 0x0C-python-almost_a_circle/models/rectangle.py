#!/usr/bin/python3
""" Module: rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiation of instance attributes"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """ Fetches width"""
            return self.__width

        @property
        def height(self):
            """Fecthes private attribute height"""
            return self.__height

        @property
        def x(self):
            """Retrivies private attribute x"""
            return self.__x

        @property
        def y(self):
            """ Retrives private attribute y"""
            return self.__y

        @width.setter
        def width(self, value):
            """validates and assigns value to width"""
            if isinstance(value, int):
                self.__width = value
            else:
                raise TypeError("width must be an integer")

            if width <= 0:
                raise ValueError("width must be > 0")

        @height.setter
        def height(self, value):
            """Validates value and assigns to height"""
            if isinstance(value, int):
                self.__height = value
            else:
                raise TypeError("height must be an integer")

            if height <= 0:
                raise ValueError("height must be > 0")

        @x.setter
        def x(self, value):
            """ Validates value and assigns it to x"""
            if isinstance(value, int):
                self.__x = value
            else:
                raise TypeError("x must be an integer")

            if x <= 0:
                raise ValueError("x must be >= 0")

        @y.setter
        def y(self, value):
            """ Validates and assigns value to y"""
            if isinstance(value, int):
                self.__y = value
            else:
                raise TypeError("Y must be an integer")

            if y <= 0:
                raise ValueError("y must be >= 0")

        def area(self):
            """Computes area of a reactangle"""

            return self.__width * self.__height

        def display(self):
            """ Prints to stdout the Rectangle instance
            with the character #"""

            for i in range(self.__height):
                for j in range(self.__width):
                    print("#", end="")
            print()
