#!/usr/bin/python3
"""Module that creates an object from a json file"""
import json


def load_from_json_file(filename):
    """Return an object created from the contect of a json file"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
