#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Inherited class to test max integer"""
    def test_max(self):
        """Tests if the function returns the max"""
        self.assertAlmostEqual(max_integer([1, 2, 3, 1, 5]), 5)
        self.assertAlmostEqual(max_integer([1, 2, -3, 1, 5]), 5)
        self.assertAlmostEqual(max_integer([-1, -2, -3]), -1)
        self.assertAlmostEqual(max_integer([-1, 0, -2, -3]), 0)
        self.assertAlmostEqual(max_integer([0]), 0)
        self.assertAlmostEqual(max_integer([]), None)

    def test_values(self):
        """Tests if the function raises errors"""
        self.assertRaises(TypeError, max_integer, 7)
        self.assertRaises(TypeError, max_integer, ["s", 1, 2])
