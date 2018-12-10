#Class Practice
from operator import *

class Pets:
   def __init__(self, name, age, fixed):
      self.name = name
      self.age = age
      self.fixed = fixed

   def __eq__(self, other):
      return self.name == self.other and \
             self.age == self.other and \
             self.fixed == self.other

   def __repr__(self):
      return self.name + ' ' + str(self.age) + ' ' + str(self.fixed)


pet = Pets('Bailey', 7, True)
print(pet)
