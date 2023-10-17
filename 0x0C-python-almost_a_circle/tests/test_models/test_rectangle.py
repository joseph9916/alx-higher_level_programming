#!/bin/usr/python3
"""
tests for the Rectangle class
"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


r1 = Rectangle(1, 2)
r2 = Rectangle(1, 2, 3, 4, 5)
b1 = Base()
return_string = "[Rectangle] (1) 0/0 - 1/2"
display1 = "{}".format("#\n" * 2)
display2 = "{}{}".format("\n" * 4, "#\n" * 2)
r1_dictionary = {"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}

class TestRectangle(unittest.TestCase):
    """Inherited class to test rectangle objects"""
    def test_rectangle(self):
        """Tests if the rectangle class is created"""
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r2, Rectangle)
        self.assertIsInstance(b1, Base)

    def test_values(self):
        """Tests if Rectangle class values have been correctly assigned"""
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        self.assertNotEqual(r1.width, 0)
        self.assertNotEqual(r1.height, 0)

    def test_error_attributes(self):
        """Test if Rectangle class raises error when assigning wrong
        attributes"""
        self.assertRaises(ValueError, Rectangle, 0, 0, 1, 2)
        self.assertRaises(ValueError, Rectangle, 1, 2, -1, 2)
        self.assertRaises(ValueError, Rectangle, -1, 2, 1, 2)
        self.assertRaises(ValueError, Rectangle, 1, 2, 1, -2)
        self.assertRaises(TypeError, Rectangle, "0", 0, 1, 2)
        self.assertRaises(TypeError, Rectangle, 1, "0", 1, 2)
        self.assertRaises(TypeError, Rectangle, 3, 2, "1", 2)
        self.assertRaises(TypeError, Rectangle)

    def test_area(self):
        """Test area of rectangle"""
        self.assertEqual(r1.area(), 2)

    def test_str(self):
        """Test string of rectangle"""
        self.assertEqual(r1.__str__(), return_string)

    def test_display(self):
        """Test display of rectangle"""
        self.assertEqual(r1.display(), print(display1))
        self.assertEqual(r2.display(), print(display2))

    def test_to_dictionary(self):
        """Tests to dictionary of Rectangle"""
        self.assertDictEqual(r1.to_dictionary(), r1_dictionary)

    def test_update(self):
        """Tests updates of dictionary"""
        r3 = Rectangle(1, 2)
        r3.update()
        r3_string = "[Rectangle] (14) 0/0 - 1/2"
        self.assertEqual(r3.__str__(), r3_string)
        r3.update(89)
        r3_string = "[Rectangle] (89) 0/0 - 1/2"
        self.assertEqual(r3.__str__(), r3_string)
        r3.update(89, 4)
        r3_string = "[Rectangle] (89) 0/0 - 4/2"
        self.assertEqual(r3.__str__(), r3_string)
        r3.update(89, 4, 5)
        r3_string = "[Rectangle] (89) 0/0 - 4/5"
        self.assertEqual(r3.__str__(), r3_string)
        r3.update(89, 4, 5, 1)
        r3_string = "[Rectangle] (89) 1/0 - 4/5"
        self.assertEqual(r3.__str__(), r3_string)
        r3.update(89, 4, 5, 1, 2)
        r3_string = "[Rectangle] (89) 1/2 - 4/5"
        self.assertEqual(r3.__str__(), r3_string)
        r4 = Rectangle(1, 2)
        r4.update(**{"id": 100})
        r4_string = "[Rectangle] (100) 0/0 - 1/2"
        self.assertEqual(r4.__str__(), r4_string)
        r4.update(**{"id": 100, "width": 4})
        r4_string = "[Rectangle] (100) 0/0 - 4/2"
        self.assertEqual(r4.__str__(), r4_string)
        r4.update(**{"id": 100, "width": 4, "height": 5})
        r4_string = "[Rectangle] (100) 0/0 - 4/5"
        self.assertEqual(r4.__str__(), r4_string)
        r4.update(**{"id": 100, "width": 4, "height": 5, "x": 2})
        r4_string = "[Rectangle] (100) 2/0 - 4/5"
        self.assertEqual(r4.__str__(), r4_string)
        r4.update(**{"id": 100, "width": 4, "height": 5, "x": 2, "y": 3})
        r4_string = "[Rectangle] (100) 2/3 - 4/5"
        self.assertEqual(r4.__str__(), r4_string)

    def test_create(self):
        """Tests if Rectangle creates method creates a rectangle"""
        r5 = Rectangle.create(**{'id': 89, 'width': 4})
        r5_string = "[Rectangle] (89) 0/0 - 4/2"
        self.assertEqual(r5.__str__(), r5_string)
        r6 = Rectangle.create(**{'id': 89})
        r6_string = "[Rectangle] (89) 0/0 - 1/2"
        self.assertEqual(r5.__str__(), r5_string)
        r7 = Rectangle.create(**{'id': 89, 'width': 4, "height": 3})
        r7_string = "[Rectangle] (89) 0/0 - 4/3"
        self.assertEqual(r7.__str__(), r7_string)
        r8 = Rectangle.create(**{'id': 89, 'width': 4, "height": 3, "x": 1})
        r8_string = "[Rectangle] (89) 1/0 - 4/3"
        self.assertEqual(r8.__str__(), r8_string)
        r9 = Rectangle.create(**{'id': 89, 'width': 4, "height": 3, "x": 1, "y": 2})
        r9_string = "[Rectangle] (89) 1/2 - 4/3"
        self.assertEqual(r9.__str__(), r9_string)


if __name__ == "__main__":
    unittest.main()
