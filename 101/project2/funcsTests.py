import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
   def test_updateAccel(self):
      self.assertEqual(updateAcceleration(1.62, 9), 1.2960000000000003)
   def test_updateAccel_2(self):
      self.assertEqual(updateAcceleration(1.62, 0), -1.62)
   def test_updateAccel_3(self):
      self.assertEqual(updateAcceleration(1.62, 2), -0.972)


   def test_updateAltitude(self):
      self.assertEqual(updateAltitude(20, 1, 1.916), 21.958)
   def test_updateAltitude_2(self):
      self.assertEqual(updateAltitude(5, 20.55, 0), 25.55)
   def test_updateAltitude_3(self):
      self.assertEqual(updateAltitude(0, -1.4, 5), 0)
   def test_updateAltitude_4(self):
      self.assertEqual(updateAltitude(32.56, -1.55, 12), 37.010000000000005)
   
   def test_updateVel(self):
      self.assertEqual(updateVelocity(13.45, -1.41), 12.04)
   def test_updateVel_2(self):
      self.assertEqual(updateVelocity(-12.05, 6.34), -5.710000000000001)   
   def test_updateVel_3(self):
      self.assertEqual(updateVelocity(0, -5.0), -5.0)   

 
   def test_updateFuel(self):
      self.assertEqual(updateFuel(35, 9), 26)
   def test_updateFuel_2(self):
      self.assertEqual(updateFuel(4, 5), 0)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

