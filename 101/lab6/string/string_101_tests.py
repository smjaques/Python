import unittest
from string_101 import *

class TestString(unittest.TestCase):
   def test_rot(self):
      string = 'hi!'
      self.assertEqual(str_rot_13(string), 'uv!')
   def test_rot2(self):
      string = 'goodbye'
      self.assertEqual(str_rot_13(string), 'tbbqolr')


   def test_trans(self):
      string = 'jajajajaja'
      old = 'j'
      new = 'h'
      self.assertEqual(str_translate_101(string, old, new), 'hahahahaha')
   def test_trans1(self):
      string = 'sydneyjaques'
      old = 's'
      new = 'm'
      self.assertEqual(str_translate_101(string, old, new), 'mydneyjaquem')



if __name__ == '__main__':
   unittest.main()

