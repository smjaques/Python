
#Project 2 - Moonlander

#NAME: Sydney Jaques
#Instructor: Workman


from landerFuncs import *


showWelcome()
altitude = getAltitude()
currentFuel = getFuel()
velocity = 0
print("\nLM state at retrorocket cutoff")
displayLMState(0, altitude, velocity, currentFuel, 0)

#after initial prompting, write loop... (find out exit condition)
#most functions will be in the loop
elapsedTime = 1
while altitude > 0 and currentFuel > 0:
   fuelRate = getFuelRate(currentFuel)
   fuelAmount = updateFuel(currentFuel, fuelRate)
   gravity = 1.62
   acceleration = updateAcceleration(gravity, fuelRate)
   altitude = updateAltitude(altitude, velocity, acceleration)
   velocity = updateVelocity(velocity, acceleration)
   if fuelAmount > 0 and altitude > 0:
      displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)
   elapsedTime = elapsedTime + 1
   currentFuel = fuelAmount
   

elapsedTime = elapsedTime - 1
while currentFuel <= 0 and altitude > 0:
   print("OUT OF FUEL - Elapsed Time:", "%3s" %elapsedTime, "Altitude:", "%7.2f" %altitude, "Velocity:","%7.2f" %velocity)
   fuelRate = 0
   gravity = 1.62
   acceleration = updateAcceleration(gravity, fuelRate)
   altitude = updateAltitude(altitude, velocity, acceleration)
   velocity = updateVelocity(velocity, acceleration)
   elapsedTime = elapsedTime + 1
   
#display lm state at landing
if altitude <= 0:
   print("\nLM state at landing/impact")
   print("{:>13s}{:>4d}{:s}".format("Elapsed Time: " ,elapsedTime, " s"))
   print("{:>14s}{:>4d}{:s}".format("Fuel: ", fuelAmount, " l"))
   print("{:>14s}{:>4d}{:s}".format("Rate: ", fuelRate, " l/s"))
   if altitude < 0:
      altitude = 0 
   print("{:>14s}{:>7s}{:s}".format("Altitude: ", "%.2f" %altitude,  " m"))
   print("{:>14s}{:>7s}{:s}".format("Velocity: ", "%.2f" % velocity, " m/s\n"))
#acceleration, altitude, velocity
   displayLMLandingStatus(velocity)
