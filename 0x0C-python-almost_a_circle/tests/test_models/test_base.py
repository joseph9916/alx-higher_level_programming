#!/bin/usr/python3
"""
tests for the base class
"""


import unittest
from models.base import Base


b1 = Base()
b2 = Base()
b3 = Base(97)
b4 = Base()
dictionary = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
json_string = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'

class TestBase(unittest.TestCase):
    """Inherited class to test base"""
    def test_base(self):
        """Tests if the base class is created and id is assigned accurately"""
        self.assertIsInstance(b1, Base)
        self.assertIsInstance(b2, Base)

    def test_values(self):
        """Test if the base class values have been updated"""
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 97)
        self.assertEqual(b4.id, 3)
        self.assertNotEqual(b1.id, None)

    def test_to_json_string(self):
        """Test to_json_string"""
        self.assertEqual(Base.to_json_string([dictionary]), json_string)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string(self):
        """Test from_json_string"""
        self.assertEqual(Base.from_json_string(json_string), [dictionary])
        self.assertEqual(Base.from_json_string("[]"), [])


if __name__ == "__main__":
    unittest.main()
