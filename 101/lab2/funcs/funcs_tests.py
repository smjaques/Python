import unittest
import funcs
import math

class TestCases(unittest.TestCase):
   def test_f_1(self):
      # Add code here. REMOVE PASS
      self.assertEqual(funcs.f(0), 0)
      self.assertEqual(funcs.f(1), 9)

   def test_f_2(self):
      # Add code here. REMOVE PASS
      self.assertEqual(funcs.f(2), 32)

   def test_g_1(self):
      # Add code here. REMOVE PASS
      self.assertEqual(funcs.g(1, 2), 5/3)
   
   def test_g_2(self):
      self.assertEqual(funcs.g(0, 0), 0)
   # Add five more tests...

   def test_h_1(self):
      self.assertEqual(funcs.hypotenuse(1, 0), 1)

   def test_h_2(self):
      self.assertEqual(funcs.hypotenuse(2, 1), 2.23606797749979)

   def test_i_1(self):
      self.assertTrue(funcs.is_positive(2))

   def test_i_2(self):
      self.assertFalse(funcs.is_positive(-2))
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

