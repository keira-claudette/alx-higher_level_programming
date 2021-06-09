#!/usr/bin/python3
""" Tests for class Rectangle"""

import pep8
import os
import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestPep8(unittest.TestCase):
    """Tests pep8 guidelines for models/rectangle.py"""
    def test_pep8(self):
        """Tests pep8"""
        style = pep8.StyleGuide(quiet=False)
        results = 0
        files = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
        results += style.check_files(files).total_errors
        self.assertEqual(results, 0, 'Fix pep8')


class TestRectangle(unittest.TestCase):
    """ TestRectangle inherits all atrributes from unittest.TestCase"""


    def test_inheritance(self):
        rect = Rectangle(1, 1)
        self.assertIsInstance(rect, Base)
        self.assertIsInstance(rect, Rectangle)

    def test_nb_attr(self):
        rect = Rectangle(1, 1)
        self.assertTrue(hasattr(rect, 'rect.__nb_objects'))

    def test_id(self):
        rect = Rectangle(1, 1)
        self.assertTrue(hasattr(rect, 'id'))

    def test_width(self):
        rect = Rectangle(1, 1)
        self.assertTrue(hasattr(rect, 'width'))

    def test_width_value(self):
        rect = Rectangle(1, 1)
        self.assertEqual(rect.width, 1)

    def test_width_string(self):
        self.assertRaises(TypeError, Rectangle, "string", 1)
        self.assertRaisesRegex(TypeError, "width must be an integer", Rectangle,
                               "string", 1)

    def test_width_neg(self):
        self.assertRaises(ValueError, Rectangle, -1, 1)
        self.assertRaisesRegex(ValueError, "width must be > 0", Rectangle, -1,
                               1)

    def test_height(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'height'))

    def test_height_value(self):
        r0 = Rectangle(1, 1)
        self.assertEqual(r0.height, 1)

    def test_height_string(self):
        self.assertRaises(TypeError, Rectangle, 1, "string")
        self.assertRaisesRegex(TypeError, "height must be an integer",
                               Rectangle, 1, "string")

    def test_height_neg(self):
        self.assertRaises(ValueError, Rectangle, 1, -1)
        self.assertRaisesRegex(ValueError, "height must be > 0", Rectangle, 1,
                               -1)

    def test_x(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'x'))

    def test_x_value(self):
        r0 = Rectangle(1, 1, 1)
        self.assertEqual(r0.x, 1)

    def test_x_string(self):
        self.assertRaises(TypeError, Rectangle, 1, 1, "string")
        self.assertRaisesRegex(TypeError, "x must be an integer", Rectangle, 1,
                               1, "string")

    def test_x_neg(self):
        self.assertRaises(ValueError, Rectangle, 1, 1, -1)
        self.assertRaisesRegex(ValueError, "x must be >= 0", Rectangle, 1, 1,
                               -1)

    def test_y(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'y'))

    def test_y_value(self):
        r0 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r0.y, 1)

    def test_y_string(self):
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, "string")
        self.assertRaisesRegex(TypeError, "y must be an integer",
                                Rectangle, 1, 1, 1, "string")

    def test_y_neg(self):
        self.assertRaises(ValueError, Rectangle, 1, 1, 1, -1)
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               Rectangle, 1, 1, 1, -1)

    def test_automatic(self):
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(1, 1)
        self.assertEqual(r3.id, 3)
        r4 = Rectangle(1, 1)
        self.assertEqual(r4.id, 4)
        r5 = Rectangle(1, 1)
        self.assertEqual(r5.id, 5)

    def test_manual(self):
        r1 = Rectangle(1, 1, 0, 0, 45)
        self.assertEqual(r1.id, 45)
        r2 = Rectangle(1, 1, 0, 0, 56)
        self.assertEqual(r2.id, 56)
        r3 = Rectangle(1, 1, 0, 0, 67)
        self.assertEqual(r3.id, 67)
        r4 = Rectangle(1, 1, 0, 0, 78)
        self.assertEqual(r4.id, 78)
        r5 = Rectangle(1, 1, 0, 0, 89)
        self.assertEqual(r5.id, 89)

    def test_mixed(self):
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(1, 1, 0, 0, 56)
        self.assertEqual(r2.id, 56)
        r3 = Rectangle(1, 1)
        self.assertEqual(r3.id, 2)
        r4 = Rectangle(1, 1, 0, 0, 78)
        self.assertEqual(r4.id, 78)
        r5 = Rectangle(1, 1)
        self.assertEqual(r5.id, 3)

    def test_area(self):
        rect_1 = Rectangle(5, 4, 1, 1)
        rect_2 = Rectangle('-5', 4, 1, 1)
        rect_3 = Rectangle(-5, 4, 1, 1)
        self.assertEqual(rect_1.area(), 20)
        with self.assertRaises(TypeError):
            rect_2.area()

        with self.assertRaises(ValueError):
            rect_3.area()

    def test_display(self):
        r0 = Rectangle(1, 1)
        self.assertTrue(hasattr(r0, 'display'))
