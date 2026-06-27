#!/usr/bin/python3
"""Module defining CountedIterator class"""


class CountedIterator:
    """An iterator that keeps track of how many items have been iterated"""

    def __init__(self, iterable):
        """Initializes with an iterable and sets counter to 0"""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Returns the number of items iterated so far"""
        return self.count

    def __next__(self):
        """Fetches next item and increments counter"""
        item = next(self.iterator)
        self.count += 1
        return item
