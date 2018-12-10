import unittest
import poly

class TestPoly(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)


   def test_poly2(self):
      list1 = [1, 2, 3]
      list2 = [4, 5, 6]
      sum = poly.poly_add2(list1, list2)
      self.assertListAlmostEqual(sum, [5, 7, 9])
   def test_poly2_2(self):
      list1 = [1.2, 3, 10]
      list2 = [4, 1.5, 5.1]
      sum = poly.poly_add2(list1, list2)
      self.assertListAlmostEqual(sum, [5.2, 4.5, 15.1])
  

   def test_mult2(self):
      first = [1, 2, 3]
      second = [1, 2, 3]
      mult = poly.poly_mult2(first, second)
      self.assertListAlmostEqual(mult, [1, 4, 10, 12, 9])
   def test_mult3(self):
      first = [3, 4, 5]
      second = [1, 1, 1]
      mult = poly.poly_mult2(first, second)
      self.assertListAlmostEqual(mult, [3, 7, 12, 9, 5])




 # Add tests here

if __name__ == '__main__':
   unittest.main()
