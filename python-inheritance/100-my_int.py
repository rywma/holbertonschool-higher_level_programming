#!/usr/bin/python3
"""Module that defines MyInt class with inverted == and != operators"""


class MyInt(int):
    """A rebel int class with inverted equality operators"""

    def __eq__(self, other):
        """Inverted == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverted != operator"""
        return super().__eq__(other)
