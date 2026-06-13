#!/usr/bin/python3
"""Module that prints a square with the character #.

This module provides a function to print a square of
a given size using the hash character.
"""


def print_square(size):
    """Print a square with the # character.

    Raises TypeError if size is not an integer.
    Raises ValueError if size is less than 0.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
