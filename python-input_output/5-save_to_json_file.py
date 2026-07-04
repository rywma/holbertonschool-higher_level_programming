#!/usr/bin/python3
"""Module that saves an object to a text file using json represetnation"""
import json


def save_to_json_file(my_obj, filename):
    """Write the json represenation of an object to a text file."""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
