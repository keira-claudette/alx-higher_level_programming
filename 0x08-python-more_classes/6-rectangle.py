#!/usr/bin/python3
"""
This module contains a Rectangle class
"""


class Rectangle:
    """ This class defines a Rectangle. It takes two attributes
    width and height which are bot integers
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ initializes a Rectangle instance

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """

        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >=0")
            self.__width = width
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >=0")
            self.__height = height
        else:
            raise TypeError("height must be an integer")
        Rectangle.number_of_instances += 1

    def __str__(self):
        """This method returns the rectangle represented by #"""
        if self.height == 0 or self.width == 0:
            return ''
        rect = ''
        for i in range(self.height):
            for j in range(self.width):
                rect = rect + '#'
            rect = rect + '\n'
        return rect[:-1]

    def __repr__(self):
        """ This method returns a string representation of the the rectangle
        to be able to create a new instance using eval()"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ deletes an instance  and prints message
        after deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """ This is a getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ This assigns value to width"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >=0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ This retrives the private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ This assigns a new value to attribute height"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >=0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """ This method returns the area of the Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """ This method returns the perimeter of the Rectangle"""
        if self.__height == 0 and self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2
