#classes

class Point:
   def __init__(self, x=0, y=0):
      self.x = x
      self.y = y
  #to override == operator in order to test if two points have same values

   def __eq__(self, other):
      return self.x == other.x and self.y == other.y

