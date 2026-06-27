#!/usr/bin/python3
"""Module that defines inherits_from function"""


def inherits_from(obj, a_class):
    """Returns True of obj inherited from a_class but is not exact"""
    return isinstance(obj, a_class) and type(obj) is not a_class
