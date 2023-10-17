#!/bin/usr/python3
"""
tests for the Rectangle class
"""


import unittest
from models.square import Square
from models.base import Base


s1 = Square(1)
s2 = Square(3, 2, 3, 5)
b1 = Base()
return_string = "[Square] (5) 0/0 - 1"
display1 = "{}".format("#\n" * 2)
display2 = "{}{}".format("\n" * 3, "  ###\n" * 3)
s1_dictionary = {"id": 5, "size": 1, "x": 0, "y": 0}

class TestRectangle(unittest.TestCase):
    """Inherited class to test rectangle objects"""
    def test_rectangle(self):
        """Tests if the rectangle class is created"""
        self.assertIsInstance(s1, Square)
        self.assertIsInstance(s2, Square)
        self.assertIsInstance(b1, Base)

    def test_values(self):
        """Tests if Rectangle class values have been correctly assigned"""
        self.assertEqual(s1.id, 5)
        self.assertEqual(s2.id, 5)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertNotEqual(s1.size, 0)

    def test_error_attributes(self):
        """Test if Rectangle class raises error when assigning wrong
        attributes"""
        self.assertRaises(ValueError, Square, 0, 0, 1, 2)
        self.assertRaises(ValueError, Square, 1, 2, -1, 2)
        self.assertRaises(ValueError, Square, -1, 2, 1, 2)
        self.assertRaises(ValueError, Square, 1, -2, 1, 2)
        self.assertRaises(TypeError, Square, "0", 0, 1, 2)
        self.assertRaises(TypeError, Square, 1, "0", 1, 2)
        self.assertRaises(TypeError, Square, 3, 2, "1", 2)
        self.assertRaises(TypeError, Square)

    def test_area(self):
        """Test area of rectangle"""
        self.assertEqual(s1.area(), 1)

    def test_str(self):
        """Test string of rectangle"""
        self.assertEqual(s1.__str__(), return_string)

    def test_display(self):
        """Test display of rectangle"""
        self.assertEqual(s1.display(), print(display1))
        self.assertEqual(s2.display(), print(display2))

    def test_to_dictionary(self):
        """Tests to dictionary of Rectangle"""
        self.assertDictEqual(s1.to_dictionary(), s1_dictionary)

    def test_update(self):
        """Tests updates of dictionary"""
        s3 = Square(2)
        s3.update()
        s3_string = "[Square] (10) 0/0 - 2"
        self.assertEqual(s3.__str__(), s3_string)
        s3.update(89)
        s3_string = "[Square] (89) 0/0 - 2"
        self.assertEqual(s3.__str__(), s3_string)
        s3.update(89, 4)
        s3_string = "[Square] (89) 0/0 - 4"
        self.assertEqual(s3.__str__(), s3_string)
        s3.update(89, 4, 5)
        s3_string = "[Square] (89) 5/0 - 4"
        self.assertEqual(s3.__str__(), s3_string)
        s3.update(89, 4, 5, 1)
        s3_string = "[Square] (89) 5/1 - 4"
        self.assertEqual(s3.__str__(), s3_string)
        s4 = Square(3)
        s4.update(**{"id": 100})
        s4_string = "[Square] (100) 0/0 - 3"
        self.assertEqual(s4.__str__(), s4_string)
        s4.update(**{"id": 100, "size": 4})
        s4_string = "[Square] (100) 0/0 - 4"
        self.assertEqual(s4.__str__(), s4_string)
        s4.update(**{"id": 100, "size": 4, "x": 2})
        s4_string = "[Square] (100) 2/0 - 4"
        self.assertEqual(s4.__str__(), s4_string)
        s4.update(**{"id": 100, "size": 5, "x": 2, "y": 3})
        s4_string = "[Square] (100) 2/3 - 5"
        self.assertEqual(s4.__str__(), s4_string)

    def test_create(self):
        """Tests if Rectangle creates method creates a rectangle"""
        s5 = Square.create(**{'id': 89, 'size': 4})
        s5_string = "[Square] (89) 2/0 - 4"
        self.assertEqual(s5.__str__(), s5_string)
        s6 = Square.create(**{'id': 89})
        s6_string = "[Square] (89) 2/0 - 1"
        self.assertEqual(s6.__str__(), s6_string)
        s7 = Square.create(**{'id': 89, 'size': 4, "x": 1})
        s7_string = "[Square] (89) 1/0 - 4"
        self.assertEqual(s7.__str__(), s7_string)
        s8 = Square.create(**{'id': 89, 'size': 3, "x": 1, "y": 2})
        s8_string = "[Square] (89) 1/2 - 3"
        self.assertEqual(s8.__str__(), s8_string)


if __name__ == "__main__":
    unittest.main()         
