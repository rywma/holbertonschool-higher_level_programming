#!/usr/bin/python3
"""Module that inserts a line after each line containing a search string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing search_string

    reads filename  and for every line that contains search_string,
    inserts new_string immediately after it and rewrites the file.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, mode="w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
