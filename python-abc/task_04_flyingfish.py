#!/usr/bin/python3
"""Module defining Fish, Bird and FlyingFish classes"""


class Fish:
    """A class representing a fish"""

    def swim(self):
        """Prints swimming message"""
        print("The fish is swimming")

    def habitat(self):
        """Prints habitat message"""
        print("The fish lives in water")


class Bird:
    """A class representing a bird"""

    def fly(self):
        """Prints flying message"""
        print("The bird is flying")

    def habitat(self):
        """Prints habitat message"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish with multiple inheritance"""

    def swim(self):
        """Prints flying fish swimming message"""
        print("The flying fish is swimming!")

    def fly(self):
        """Prints flying fish soaring message"""
        print("The flying fish is soaring!")

    def habitat(self):
        """Prints flying fish habitat message"""
        print("The flying fish lives both in water and the sky!")
