import unittest
from objects import *
from funcs_objects import *

class TestCases(unittest.TestCase):
   def test_point(self):
      pt1 = Point(3, 6)
      self.assertAlmostEqual(pt1.x, 3)
      self.assertAlmostEqual(pt1.y, 6)
   def test_point1(self):
      pt1 = Point(5, 9)
      self.assertAlmostEqual(pt1.x, 5)
      self.assertAlmostEqual(pt1.y, 9)
   def test_point2(self):
      pt1 = Point(-1.345, 3.8)
      self.assertAlmostEqual(pt1.x, -1.345)
      self.assertAlmostEqual(pt1.y, 3.8)


   def test_distance(self):
      pt1 = Point(5, 10)
      pt2 = Point(2, 6)
      self.assertEqual(distance(pt1, pt2), 5)
   def test_distance1(self):
      pt1 = Point(-12.3, 5)
      pt2 = Point(0, -5)
      self.assertEqual(distance(pt1, pt2), 15.852129194527782)
   def test_distance2(self):
      pt1 = Point(1.453, 3.4)
      pt2 = Point(-233.4, -2.45)
      self.assertEqual(distance(pt1, pt2), 234.9258481074401)


   def test_circle(self):
      circle1 = Circle(Point(1, 1), 1)
      circle2 = Circle(Point(10, 2), 1)
      self.assertFalse(circles_overlap(circle1, circle2))
   def test_circle2(self):
      circle1 = Circle(Point(-1.346, 45), 2)
      circle2 = Circle(Point(456.3, -12.34), 35)
      self.assertFalse(circles_overlap(circle1, circle2))
   def test_circle3(self):
      circle1 = Circle(Point(0, 0), 10)
      circle2 = Circle(Point(0, 0), 5)
      self.assertTrue(circles_overlap(circle1, circle2))

   # Add other testing functions


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

