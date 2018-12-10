#tests for classes

import unittest
from feb27 import *

class PointTests(unittest.TestCase):
   def test_points_equal(self):
      pt1 = Point(1.234, -8)
      pt2 = Point(1.234, -8)
      self.assertEqual(pt1, pt2)
   def test_points_equal2(self):
      pt1 = Point(1.234, -8)
      pt2 = Point(1.233, -8)
      self.assertNotEqual(pt1, pt2)






if __name__ == '__main__':
   unittest.main()
