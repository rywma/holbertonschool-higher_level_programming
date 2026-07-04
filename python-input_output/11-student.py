#!/usr/bin/python3
"""Module that defines a Student class that can be saved and reloaded."""


class Student:
    """Represent a student with a first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of this Student instance.

        If attrs is a list of strings only include attributes
        whose names appear in that list. Otherwise include all
        attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of this instance from a dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
