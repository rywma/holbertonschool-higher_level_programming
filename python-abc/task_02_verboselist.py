#!/usr/bin/python3
"""Module defining VerboseList class that extends list"""


class VerboseList(list):
    """A list subclass that prints notifications on modifications"""

    def append(self, item):
        """Adds item and prints notification"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extends list and prints notification"""
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Remove item and print notification"""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops item and print notification"""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
