#!/usr/bin/python3
"""
Defines a function that writes to a text file
"""


def write_file(filename="", text=""):
    """Writes to a text file.
    Args:
        filename - name of the file
        text - string to write to text file
    Return: number of characters
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
