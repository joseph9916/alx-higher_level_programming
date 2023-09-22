#!/usr/bin/python3
"""
tests for the base class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


r1 = Rectangle(10, 2)
r2 = Rectangle(5, 3)
r3 = Rectangle(10, 2, 1, 1, 12)

class TestBase(unittest.TestCase):
    """Inherited class to test max integer"""
    def test_rect(self):
        """Tests if the base class is created and id is assigned accurately"""
        self.assertIsInstance(r1, Base)
        self.assertIsInstance(r2, Rectangle)

    def test_init_rectangle(self):
        """Test  the initialising of rectangle"""
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r3, Rectangle)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_raise_error(self):
        """Test if it raises errors"""
        self.assertRaises(TypeError, Rectangle, ("1", "2"))

    #def test_value_error(self):
        """Test if it raises errors"""
     #   self.assertRaises(ValueError, Rectangle, (1, -2))

    def test_area(self):
        self.assertAlmostEqual(r1.area(), 20)
        self.assertAlmostEqual(r2.area(), 15)

    def test_update(self):
        """test updates"""
        vals = (6, 6, 20, 7, 8)
        r1.update(*vals)
        self.assertAlmostEqual(r1.id, 6)
        self.assertAlmostEqual(r1.width, 6)
        self.assertAlmostEqual(r1.height, 20)
        self.assertAlmostEqual(r1.x, 7)
        self.assertAlmostEqual(r1.y, 8)
        kwargs = {"id": 1, "width": 3, "height": 4, "x": 3, "y": 5}
        r1.update(**kwargs)
        self.assertAlmostEqual(r1.id, 1)
        self.assertAlmostEqual(r1.width, 3)
        self.assertAlmostEqual(r1.height, 4)
        self.assertAlmostEqual(r1.x, 3)
        self.assertAlmostEqual(r1.y, 5)
        kwargs = {"width": -2}
        self.assertRaises(ValueError, r1.update, **kwargs)
        kwargs = {"width": "i"}
        self.assertRaises(TypeError, r1.update, **kwargs)
        args = (3, -2, 3)
        self.assertRaises(ValueError, r1.update, *args)
