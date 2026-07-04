#!/usr/bin/python3
"""Module that appends a string to the end of a text file."""


def append_write(filename="", text=""):
    """Append a string to a text file (UTF8) and return chars added."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
