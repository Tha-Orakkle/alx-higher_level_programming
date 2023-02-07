#!/usr/bin/python3

"""
Defines a function that checks the class of an object
"""


def is_same_class(obj, a_class):
    """checks if the object is exactly an
    instance of a specific class

    Args:
        obj: the object to check
        a_class: The class to match the type of the obj with
    Returns:
        if obj is exactly an instance of a_class - True
        Otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    return False
