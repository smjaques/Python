import unittest
import filter


class TestCases(unittest.TestCase):
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)


   def test_1(self):
      list1 = [-12, 3, -5, 3, 1, 9]
      list2 = filter.are_positive(list1)
      self.assertListAlmostEqual(list2, [3, 3, 1, 9])
   def test_2_positive(self):
      list1 = [-12, 0, 56, -72, 4, -20]
      list2 = filter.are_positive(list1)
      self.assertListAlmostEqual(list2, [56, 4]) 


   def test_greater(self):      
      list1 = [-3, 5, 100, 27, 7]
      n = 21
      list2 = filter.are_greater_than_n(list1, n)
      self.assertListAlmostEqual(list2, [100, 27])
   def test_greater_2(self):
      list1 = [5, 13, 943, -34, 6, 1048, 20, -40]
      n = 20
      list2 = filter.are_greater_than_n(list1, n)
      self.assertListAlmostEqual(list2, [943, 1048])


   def test_divisible(self):
      list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      n = 2
      list2 = filter.are_divisible_by_n(list1, n)
      self.assertListAlmostEqual(list2, [2, 4, 6, 8, 10])
   def test_divisible_2(self):
      list1 = [20, 55, 32, 43, 67, 55, 100, 74]
      n = 5
      list2 = filter.are_divisible_by_n(list1, n)
      self.assertListAlmostEqual(list2, [20, 55, 55, 100])




# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

