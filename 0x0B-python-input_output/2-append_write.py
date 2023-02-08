#!/usr/bin/python3
"""
Defines a function that appends to a text file
"""


def append_write(filename="", text=""):
    """appends to the end of a text file
    Args:
        filename (str) - name of the text file to append to
        text (str) - string to append
    Return: number of characters appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
