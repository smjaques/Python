import unittest
from fold import *

class TestCases(unittest.TestCase):
   def test_1(self):
      list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
      self.assertEqual(sum(list1), 45)
   def test_2(self):
      list1 = [5, 7, -4, 2, 10]
      self.assertEqual(sum(list1), 20)

   def test_small(self):
      list1 = [-1, 3, 6, 2, -5]
      self.assertEqual(index_of_smallest(list1), 4)
   def test_small1(self):
      list1 = []
      self.assertEqual(index_of_smallest(list1), -1)
   def test_small2(self):
      list1 = [-103, 4, 9866, -200, 4, 5, 7]
      self.assertEqual(index_of_smallest(list1), 3)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

