#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the max_integer function.
    """

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test a list of mixed positive and negative numbers."""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_duplicate_numbers(self):
        """Test a list with duplicate numbers."""
        self.assertEqual(max_integer([1, 2, 2, 3]), 3)

    def test_floats(self):
        """Test a list of floating-point numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_mixed_types(self):
        """Test a list with mixed types (int and float)."""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)

    def test_large_numbers(self):
        """Test a list with large numbers."""
        self.assertEqual(max_integer([1000000, 2000000, 3000000]), 3000000)

    def test_strings(self):
        """Test a list of strings (should raise TypeError)."""
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

    def test_none(self):
        """Test passing None as an argument (should raise TypeError)."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_list(self):
        """Test passing a non-list argument (should raise TypeError)."""
        with self.assertRaises(TypeError):
            max_integer(123)

if __name__ == "__main__":
    unittest.main()
