#!/usr/bin/python3
"""Module that defines Rectangle class with area and str"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class with area and str represenation"""

    def __init__(self, width, height):
        """Initializes Rectangle with validated width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
