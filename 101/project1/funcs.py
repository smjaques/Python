
# Project 1

# Name:  Sydney Jaques
# Instructor: J. Workman
#Section: 05

import math

def getMassObject(object):
   if object == "t":
      massObject = 0.1
   elif object == "p":
      massObject = 1.0
   elif object == "r":
      massObject = 3.0
   elif object == "g":
      massObject = 5.3
   elif object == "l":
      massObject = 9.07
   else:
      return(0)
   return(massObject)

def getVelocityObject(distance):
   return (math.sqrt(9.8 * distance / 2))

def getVelocitySkater(massSkater, massObject, velObject):
   if massSkater > 0:
      return((massObject * velObject) / massSkater)
   elif massSkater <= 0:
      return("-nan")

def poundsToKG(pounds):
   return(pounds * 0.453592)

