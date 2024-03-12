"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import math
import unittest
from circle import Circle

class CircleTest(unittest.TestCase):
    def test_add_area_normal(self):
        circle1 = Circle(5)
        circle2 = Circle(10)
        self.assertEqual(Circle(math.hypot(circle1.radius, circle2.radius)).radius,
                         circle1.add_area(circle2).radius)

    def test_add_area_abnormal(self):
        circle1 = Circle(0)
        circle2 = Circle(5)
        self.assertEqual(Circle(5).radius, circle1.add_area(circle2).radius)

    def test_negative_radius(self):
        with self.assertRaises(Exception):
            circle1 = Circle(-1)
