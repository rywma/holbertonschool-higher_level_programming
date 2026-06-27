#!/usr/bin/python3
"""Module defining Animal abstract class and its subclasses"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals"""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses"""
        pass


class Dog(Animal):
    """Dog class inheriting from Animal"""

    def sound(self):
        """Returns the sound a dog makes"""
        return "Bark"


class Cat(Animal):
    """Cat class inheriting from Animal"""

    def sound(self):
        """Returns the ound a cat makes"""
        return "Meow"
