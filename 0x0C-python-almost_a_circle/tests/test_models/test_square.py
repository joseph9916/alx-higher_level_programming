#!/usr/bin/python3
"""
tests for the base class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


s1 = Square(10)
s2 = Square(5, 3, 1, 2)

class TestBase(unittest.TestCase):
    """Inherited class to test max integer"""
    def test_rect(self):
        """Tests if the base class is created and id is assigned accurately"""
        self.assertIsInstance(s1, Square)
        self.assertIsInstance(s2, Rectangle)

    def test_init_rectangle(self):
        """Test  the initialising of rectangle"""
        self.assertEqual(s1.id, 5)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 1)

    def test_raise_error(self):
        """Test if it raises errors"""
        self.assertRaises(TypeError, Square, ("1"))

    #def test_value_error(self):
        """Test if it raises errors"""
     #   self.assertRaises(ValueError, Rectangle, (1, -2))

    def test_area(self):
        self.assertAlmostEqual(s1.area(), 100)
        self.assertAlmostEqual(s2.area(), 25)

    def test_update(self):
        """test updates"""
        s1.update(6, 6, 7, 8)
        self.assertAlmostEqual(s1.id, 6)
        self.assertAlmostEqual(s1.size, 6)
        self.assertAlmostEqual(s1.x, 7)
        self.assertAlmostEqual(s1.y, 8)
        kwargs = {"id": 1, "size": 3, "x": 3, "y": 5}
        s1.update(**kwargs)
        self.assertAlmostEqual(s1.id, 1)
        self.assertAlmostEqual(s1.size, 3)
        self.assertAlmostEqual(s1.x, 3)
        self.assertAlmostEqual(s1.y, 5)
        kwargs = {"size": -2}
        self.assertRaises(ValueError, s1.update, **kwargs)
        kwargs = {"size": "i"}
        self.assertRaises(TypeError, s1.update, **kwargs)
        args = (3, -2, 3)
        self.assertRaises(ValueError, s1.update, *args)

    def test_to_dictionary(self):
        """Tests if class is converted to dictionary"""
        s3 = Square(3, 3, 4, 4)
        (self.assertDictEqual(s3.to_dictionary(),
            {"size": 3, "x": 3, "y" :4, "id": 4}))
