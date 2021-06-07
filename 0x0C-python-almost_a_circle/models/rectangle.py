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
        if isinstance(value, int) and value < 0:
            self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

    @height.setter
    def height(self, value):
        """Validates value and assigns to height"""
        if isinstance(value, int) and value > 0:
            self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

    @x.setter
    def x(self, value):
        """ Validates value and assigns it to x"""
        if isinstance(value, int) and value > 0:
            self.__x = value
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value <= 0:
            raise ValueError("x must be >= 0")

    @y.setter
    def y(self, value):
        """ Validates and assigns value to y"""
        if isinstance(value, int) and value > 0:
            self.__y = value
        if not isinstance(value, int):
            raise TypeError("Y must be an integer")

        if value <= 0:
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
        print()

    def __str__(self):
        """Returns a string representation of a Rectangle instance."""

        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute"""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
