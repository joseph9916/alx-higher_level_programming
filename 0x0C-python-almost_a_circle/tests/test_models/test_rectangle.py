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
r3 = Rectangle(10, 2, 1, 1, 12)

class TestBase(unittest.TestCase):
    """Inherited class to test max integer"""
    def test_base(self):
        """Tests if the base class is created and id is assigned accurately"""
        self.assertIsInstance(b1, Base)
        self.assertIsInstance(b2, Base)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 15)
        self.assertEqual(b3.id, "2")

    def test_init_rectangle(self):
        """Test  the initialising of rectangle"""
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r3, Rectangle)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 1)
