#!/usr/bin/python3
"""
A module for Square class
"""


class Square:
    """A class Square
    Private instance attribute size:
        - property def size(self)
        - property setter def size(self, value)
    Private instance attribute: position:
        - property def position(self)
        - property setter def position(self, value)
    Instantiation with optional size
    Public instance method def area(self)
    Public instance method def my_print(self)

    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the data"""
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__postion = value

    def area(self):
        """Returns the area of square"""
        return self.__size ** 2

    def my_print(self):
        """prints a square with character '#',
        at the position given by the position attribute"""
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__position[1]):
            print()
        for x in range(0, self.__size):
            for y in range(0, self.__position[0]):
                print(" ", end="")
            for z in range(0, self.__size):
                print("#", end="")
            print()
