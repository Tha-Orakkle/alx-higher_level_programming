#!/usr/bin/python3

"""Defines an inherited list class Mylist."""


class MyList(list):
    """Implements sorted printing for the built_in list class."""

    def print_sorted(self):
        """Print a llst in sorted ascending order"""
        print(sorted(self))
