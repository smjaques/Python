import unittest
import conditional

class TestCases(unittest.TestCase):
   def test_case_101_1(self):
      self.assertEqual(conditional.max_101(10, 5), 10)
   def test_case_101_2(self):
      self.assertEqual(conditional.max_101(100, 100), 100)

   def test_case_three_1(self):
      self.assertEqual(conditional.max_of_three(1.0, 3.5, 3.5), 3.5)
   def test_case_three_2(self):
      self.assertEqual(conditional.max_of_three(500.12, 12.4, 16.7), 500.12)
   def test_case_three_3(self):
      self.assertEqual(conditional.max_of_three(2.2, 1000.01, 13.3), 1000.01)

   def test_case_rental(self):
      self.assertEqual(conditional.rental_late_fee(0), 0)
      self.assertEqual(conditional.rental_late_fee(-2), 0)
   def test_case_rental(self):
      self.assertEqual(conditional.rental_late_fee(15), 7)
   def test_case_rental(self):
      self.assertEqual(conditional.rental_late_fee(100), 100)




# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

