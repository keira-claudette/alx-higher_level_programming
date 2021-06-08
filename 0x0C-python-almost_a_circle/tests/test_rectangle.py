#!/usr/bin/python3
""" Tests for class Rectangle"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ TestRectangle inherits all atrributes from unittest.TestCase"""

    def test_area(self):
        rect_1 = Rectangle(5, 4, 1, 1)

        self.assertEqual(rect_1.area(), 20)

if __name__ == '__main__':
    unittest.main()