#!/usr/bin/python3
"""Module that defines Square class with str representation"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle with str method"""

    def __init__(self, size):
        """Initializes Square with validated size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Returns string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
