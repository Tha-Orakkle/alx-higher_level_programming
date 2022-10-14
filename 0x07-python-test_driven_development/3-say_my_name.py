#!/usr/bin/python3
"""
Module say_my_name
Prints a given first name and last name.
"""


def say_my_name(first_name, last_name=""):
    """Prints a string with the given first_name
    and last_name.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
