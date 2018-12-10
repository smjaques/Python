#groups tests

from groups import *
import unittest

class TestCases(unittest.TestCase):

   def test_groups3_1(self):
      values = [3, 5, 7, 9, 3, 3, 12, 6, 89, 6]
      self.assertEqual(groups_of_3(values), [[3, 5, 7], [9, 3, 3], [12, 6, 89], [6]])

   def test_groups3_2(self):
      values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
      self.assertEqual(groups_of_3(values), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
   def test_groups3_3(self):
      values = [0, 1, 2, 3, 4]
      self.assertEqual(groups_of_3(values), [[0, 1, 2], [3, 4]])
   def test_groups3_4(self):
      values = [0, 1, 2, 3]
      self.assertEqual(groups_of_3(values), [[0, 1, 2], [3]])












if __name__ == '__main__':
   unittest.main()
