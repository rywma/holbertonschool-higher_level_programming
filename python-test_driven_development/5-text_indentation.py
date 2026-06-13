#!/usr/bin/python3
"""Module that prints text with indentation after punctuation.

This module provides a function that prints text with two
new lines after each '.', '?' or ':' character.
"""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' or ':'.

    Raises TypeError if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    for line in result.split("\n"):
        print(line.strip())
