#!/usr/bin/python3
"""
A module for Square class
"""


class Square:
    """A class Square"""
    def __init__(self, size=0):
        """initializes the data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
