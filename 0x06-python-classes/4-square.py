#!/usr/bin/python3
"""
A module for Square class
Private instance attribute size:
    - property def size(self)
    - property setter def size(self, value)
Instantiation with optional size
Public instance method def area(self)
"""


class Square:
    """A class Square"""
    def __init__(self, size=0):
        """initializes the data"""
        self.__size = size

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of square"""
        return self.__size ** 2
