import unittest
from char import *

class TestChar(unittest.TestCase):
   def test_lower(self):
      char = 'g'
      self.assertTrue(is_lower_101(char))
   def test_lower2(self):
      char = 'G'
      self.assertFalse(is_lower_101(char))


   def test_char(self):
      char = 'a'
      self.assertEqual(char_rot_13(char), 'n')
   def test_char2(self):
      char = 'z'
      self.assertEqual(char_rot_13(char), 'm')



if __name__ == '__main__':
   unittest.main()

