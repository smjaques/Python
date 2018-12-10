import unittest
from objects import *
from utility import *

class TestCases(unittest.TestCase):
   def test_equality(self):
      pt1 = Point(1, 2)
      pt2 = Point(1, 2)
      self.assertTrue(pt1 == pt2)
   def test_equality2(self):
      pt1 = Point(-3.4, 1)
      pt2 = Point(3.4, 1)
      self.assertFalse(pt1 == pt2)
   def test_equality3(self):
      pt1 = Point(-1, -4)
      pt2 = Point(-1, -4)
      self.assertTrue(pt1 == pt2)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

