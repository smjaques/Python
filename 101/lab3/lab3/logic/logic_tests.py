import unittest
import logic

class TestCases(unittest.TestCase):
   def test_case(self):
      self.assertTrue(logic.is_even(2))
   def test_case_2(self):
      self.assertFalse(logic.is_even(3))

   def test_case_i_1(self):
      self.assertTrue(logic.in_an_interval(4)) 
   def test_case_i_2(self):
      self.assertTrue(logic.in_an_interval(100))
   def test_case_i_2(self):
      self.assertTrue(logic.in_an_interval(26))
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

