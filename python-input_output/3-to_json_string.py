#!/usr/bin/python3
"""Module that converts an object to its json string representation."""
import json


def to_json_string(my_obj):
    """Return the json string representation of an object."""
    return json.dumps(my_obj)
