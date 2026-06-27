#!/usr/bin/python3
"""Module defining Shape abstract class, circle, rectangle, and shape_info"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Abstract for calculating area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract for calculating perimeter"""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape"""

    def __init__(self, radius):
        """Initializes Circle with a radius"""
        self.radius = radius

    def area(self):
        """Returns peimeter of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Returns perimeter of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape"""

    def __init__(self, width, height):
        """Initializes Rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Returns area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints area and perimeter of any shape using duck typing"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
