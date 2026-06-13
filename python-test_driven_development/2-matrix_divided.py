#!/usr/bin/python3
"""Module that divides all elements of a matrix.

This module provides a function to divide every element
of a matrix by a given divisor, rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Returns a new matrix with results rounded to 2 decimal places.
    Raises TypeError if matrix or div are invalid types.
    Raises ZeroDivisionError if div is zero.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix) or not all(
            isinstance(el, (int, float))
            for row in matrix for el in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
