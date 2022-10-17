#!/usr/bin/python3
"""
Module 6-rectangle
defines a class Rectangle
"""


class Rectangle:
    """Rectangle class defined by width and height."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialises a class rectangle instance.

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for row in range(self.__height):
            for col in range(self.__width):
                string += "#"
            string += "\n"
        return string[:-1]

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """deletes a Rectangle instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance"""
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
        """Retrieve the height of a Rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height

        Args:
            value: value of height must be a positive integer
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle instance"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of a rectangle instance.

        returns 0 if height or width == 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
