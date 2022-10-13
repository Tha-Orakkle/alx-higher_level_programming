#!/usr/bin/python3
"""
A module for Square class
"""


class Square:
    """A class Square
    Private instance attribute size:
        - property def size(self)
        - property setter def size(self, value)
    Instantiation with optional size
    Public instance method def area(self)
    Public instance method def my_print(self)

    """
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

    def my_print(self):
        """prints a square with character '#' to the stdout"""
        if self.__size == 0:
            print()
        else:
            for row in range(0, self.__size):
                for col in range(0, self.__size):
                    print("#", end="")
                print()
