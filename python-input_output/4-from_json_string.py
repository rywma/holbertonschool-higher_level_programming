#!/usr/bin/python3
"""Module that converts a json string to a python data structure."""
import json


def from_json_string(my_str):
    """Return a python object represented by a json string."""
    return json.loads(my_str)
