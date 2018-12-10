# Project 1

# Name:  Sydney Jaques
# Instuctor: J.Workman
# Section: 05

import unittest
import funcs
import math

class TestCases(unittest.TestCase):
   def test_vo_1(self):
      self.assertEqual(funcs.getVelocityObject(2), 3.1304951684997055)
   def vest_vo_2(self):
      self.assertEqual(funcs.getVelocitObject(50), 11.06797181)

   def test_vs_1(self):
      self.assertEqual(funcs.getVelocitySkater(2, 2, 2), 2)
   def test_vs_2(self):
      self.assertEqual(funcs.getVelocitySkater(130, .2, 30), 0.046153846153846156)
   def test_vs_3(self):
      self.assertEqual(funcs.getVelocitySkater(0, 1, 1), "-nan")
 
   def test_p_1(self):
      self.assertEqual(funcs.poundsToKG(134), 60.781328)
   def test_p_2(self):
      self.assertEqual(funcs.poundsToKG(20), 9.07184)
   def test_p_3(self):
      self.assertEqual(funcs.poundsToKG(100), 45.3592)

   def test_mo_1(self):
      self.assertEqual(funcs.getMassObject("t"), 0.1)
   def test_mo_2(self):
      self.assertEqual(funcs.getMassObject("p"), 1.0)
   def test_mo_3(self):
      self.assertEqual(funcs.getMassObject("r"), 3.0)
   def test_mo_4(self):
      self.assertEqual(funcs.getMassObject("g"), 5.3)
   def test_mo_5(self):
      self.assertEqual(funcs.getMassObject("l"), 9.07)
   def test_mo_6(self):
      self.assertEqual(funcs.getMassObject("e"), 0)

if __name__ == '__main__':
   unittest.main()
