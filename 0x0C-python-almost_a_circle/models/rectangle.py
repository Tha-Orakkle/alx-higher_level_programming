#!/usr/bin/python3
"""Defines class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class"""


    """
    Initialize a new Rectangle.

    Args:
        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle.
        x (int): The x coordinate of the new Rectangle.
        y (int): The y coordinate of the new Rectangle.
        id (int): The identity of the new Rectangle.
    Raises:
        TypeError: If either of width or height is not an int.
        ValueError: If either of width or height <= 0.
        TypeError: If either of x or y is not an int.
        ValueError: If either of x or y < 0.
    """
