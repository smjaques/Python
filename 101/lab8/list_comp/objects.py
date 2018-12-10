#Sydney Jaques
#Objects.py 
#Classes and Points
from utility import *

class Point:
   def __init__(self, x, y):
   #self references point
      self.x = x
      self.y = y
   def __eq__(self, otherpoint):
      return epsilon_equal(self.x, otherpoint.x)  and epsilon_equal(self.y, otherpoint.y)
class Circle:
   def __init__(self, center, radius):
      self.center = center
      self.radius = radius




