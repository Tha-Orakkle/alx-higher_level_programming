#!/usr/bin/python3
"""
Module 1-rectangle
defines a class Rectangle
"""


class Rectangle:
    """Rectangle class defined by width and height."""

    def __init__(self, width=0, height=0):
        """Initialises a class rectangle instance.

        Args:
            width: width of the rectangle
            height: height of the rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width

        Args:
            value: value of width must be a positive integer
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height

        Args:
            value: value of height must be a positive integer
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
