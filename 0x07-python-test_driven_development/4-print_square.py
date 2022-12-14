#!/usr/bin/python3
"""
Module print_square
Prints a square with the character #.
"""


def print_square(size):
    """Prints a square.
    size is the length of the square.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for col in range(size):
            print('#', end='')
        print()
