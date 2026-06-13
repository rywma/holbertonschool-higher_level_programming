#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_normal_list(self):
        """Test with a normal unsorted list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_sorted_ascending(self):
        """Test with an already sorted list ascending"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_sorted_descending(self):
        """Test with a list sorted descending"""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_single_element(self):
        """Test with a list of one element"""
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        """Test with an empty list, should return None"""
        self.assertEqual(max_integer([]), None)

    def test_default_argument(self):
        """Test calling with no argument uses default empty list"""
        self.assertEqual(max_integer(), None)

    def test_negative_numbers(self):
        """Test with all negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-5, 0, 5, -10, 10]), 10)

    def test_duplicate_max_values(self):
        """Test when max value appears multiple times"""
        self.assertEqual(max_integer([3, 7, 7, 2]), 7)

    def test_all_same_values(self):
        """Test when all values are the same"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)


if __name__ == '__main__':
    unittest.main()
