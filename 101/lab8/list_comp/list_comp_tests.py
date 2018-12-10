import unittest
from list_comp import *
from objects import *

class TestCases(unittest.TestCase):
   def test_1(self):
      p1 = Point(0, 1)
      p2 = Point(3, 4)
      p3 = Point(4, -3)
      points = [p1, p2, p3]
      output = distance_all(points)
      self.assertEqual(output[0], 1)
   def test_distance2(self):
      p1 = Point(-3, 2)
      p2 = Point(0, -5)
      p3 = Point(1, 1)
      points = [p1, p2, p3]
      output = distance_all(points)
      self.assertEqual(output[1], 5)
   def test_distance3(self):
      p1 = Point(-2, 5)
      p2 = Point(2, 1)
      p3 = Point(-12, 15)
      points = [p1, p2, p3]
      output = distance_all(points)
      self.assertEqual(output[0], 5.385164807134504)

   def test_firstquad(self):
      p1 = Point(-2, 5)
      p2 = Point(2, 3)
      p3 = Point(1, 1)
      points = [p1, p2, p3]
      self.assertListEqual(are_in_first_quadrant(points), [Point(2, 3), Point(1, 1)])
   def test_firstquad1(self):
      p1 = Point(-1, 3)
      p2 = Point(-12, -45)
      p3 = Point(0, 0)
      points = [p1, p2, p3]
      self.assertListEqual(are_in_first_quadrant(points), [])


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

