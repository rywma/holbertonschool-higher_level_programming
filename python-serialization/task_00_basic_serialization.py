#!/usr/bin/env python3
"""Module for basic serialization and deserialization of a dictionary"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to json and save it to a file.

    Args:
        data(dict): the dictionary to serialize
        filename(str): the path of the output json file. If
            file already exists it is replaced.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize json  data from a file into a dictionary.

    Args:
        filename (str): the path of the input json file.

    Returns:
        dict: the deserialized data from the file.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
