


from classes import *
import unittest

class TestCases(unittest.TestCase):
   def test_pet_init(self):
      pet1 = Pets('Charlie', 1, False)
      self.assertEqual(pet1.name, 'Charlie')
      self.assertEqual(pet1.age, 1)
      self.assertEqual(pet1.fixed, False)





if __name__ == '__main--':
   unittest.main()
