# Project 1

# Name:  Sydney Jaques
# Instructor: J.Workman
# Section: 05

import funcs
import math 

def main():
   #Ask how much skater weighs to get massSkater
   massSkater = int(input("How much do you weigh (pounds)? "))
   #use poundsToKG function to get their weight in kilograms
   mass = funcs.poundsToKG(massSkater)

   #Ask how far skater is from professor to get distance
   distance = int(input("How far away is your professor (meters)? "))
   #use distance in function  getvelocityObject
   velObject= funcs.getVelocityObject(distance)
   object = str(input("Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? "))
   massObject = funcs.getMassObject(object)
   #I have the massObject
   skatervelocity = funcs.getVelocitySkater(mass, massObject, velObject)

   #now I have all the variables... print the ending!
   print("\nNice throw! ",end ="")
   
   if massObject <= 0.1:
      print("You're going to get an F!")
   elif massObject > 0.1 and massObject <= 1.0:
      print("Make sure your professor is OK.")
   elif massObject > 1.0 and distance < 20:
      print("How far away is the hospital?")
   elif massObject > 1.0 and distance > 20:
      print("RIP professor.")  

   #this is the first line of the comments
   if skatervelocity == "-nan":
      print("Velocity of skater: -nan m/s")
   elif skatervelocity != "-nan":
      print("Velocity of skater:", "%.3f" %skatervelocity, "m/s")
      if skatervelocity < 0.2:
         print("My grandmother skates faster than you!")
      elif skatervelocity >= 0.2 and skatervelocity < 1.0:
         return ""
      elif skatervelocity >= 1.0:
         print("Look out for that railing!!!")


if __name__ == '__main__':
   main()
