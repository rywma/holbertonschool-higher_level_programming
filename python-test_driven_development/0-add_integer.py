#!/usr/bin/python3
"""Module that adds 2 integers.

This module provides a function to add two integers or floats.
Floats are cast to integers before addition.
"""


def add_integer(a, b=98):
    """Add two integers or floats, returns an integer.

    Raises TypeError if a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
