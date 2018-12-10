import unittest
import map

class TestCases(unittest.TestCase):
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_1(self):
      # Add code here.
      #list1 = [0, 0, 0]
      #list2 = [3, 4, 6]
      #list3 = map.square_all(list1, list2)
      #self.assertListAlmostEqual(list3, [3, 5, 6])
      list1 = [2, 3, 4]
      list2 = map.square_all(list1)
      self.assertListAlmostEqual(list2, [4, 9, 16])
   def test_square_2(self):
      list1 = [1, 10, 2]
      list2 = map.square_all(list1)
      self.assertListAlmostEqual(list2, [1, 100, 4])
   def test_square_3(self):
      list1 = [2.3, 5, 7.1]
      list2 = map.square_all(list1)
      self.assertListAlmostEqual(list2, [5.29, 25, 50.41])


   def test_add(self):
      list1 = [5, 10, 67]
      n = 5
      list3 = map.add_n_a(n, list1)
      self.assertListAlmostEqual(list3, [10, 15, 72])
   def test_add_2(self):
      list1 = [25, 65, 60]
      n = -4
      list3 = map.add_n_a(n, list1)
      self.assertListAlmostEqual(list3, [21, 61, 56])


   def test_evenodd(self):
      num = [2, 5, 10]
      nums2 = map.even_or_odd_all(num)
      self.assertListAlmostEqual(nums2, [True, False, True])
   def test_evenodd_2(self):
      num = [7, 1, 5]
      nums2 = map.even_or_odd_all(num)
      self.assertListAlmostEqual(nums2, [False, False, False])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

