#!/usr/bin/env python3
"""Module for serializing and deserializing objects using pickle."""
import pickle


class CustomObject:
    """Represent a custom object with a name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initialize a new CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in a readable format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize this instance and save it to filename using pickle.

        Returns None if the object cannot be serialized.
        """
        try:
            with open(filename, mode="wb") as f:
                pickle.dump(self, f)
        except (pickle.PickleError, OSError, TypeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return a CustomObject instance from filename.

        Returns None if the file doesn't exist or is malformed.
        """
        try:
            with open(filename, mode="rb") as f:
                return pickle.load(f)
        except (pickle.PickleError, OSError, EOFError,
                AttributeError, ImportError, IndexError):
            return None
