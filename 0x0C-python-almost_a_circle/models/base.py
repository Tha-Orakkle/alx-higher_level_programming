#!/usr/bin/python3
"""Defines a first class base"""


class Base:
    """The Base model

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes a new Base

        Args:
            id (int): identity of the base
        """
        if id is not  None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
