#!/usr/bin/python3
"""
tests for the base class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


b1 = Base()
b2 = Base(15)
b3 = Base("2")
r1 = Rectangle(10, 2)

class TestBase(unittest.TestCase):
    """Inherited class to test max integer"""
    def test_base(self):
        """Tests if the base class is created and id is assigned accurately"""
        self.assertIsInstance(b1, Base)
        self.assertIsInstance(b2, Base)
        self.assertIsNotInstance(r1, Base)

    def test_values(self):
        """Test if the base class values have been updated"""
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 15)
        self.assertEqual(b3.id, "2")
        self.assertNotEqual(b1.id, None)
