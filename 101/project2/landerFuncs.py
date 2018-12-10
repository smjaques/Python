# Project 2 - Moonlander
# 
# Name:  Sydney Jaques
# Instructor: Workman

def showWelcome():
   print("\nWelcome aboard the Lunar Module Flight Simulator\n")
   print("{:>54s}".format("To begin you must specify the LM's initial altitude"))
   print("{:>49s}".format("and fuel level.  To simulate the actual LM use"))
   print("{:>55s}".format("values of 1300 meters and 500 liters, respectively.\n"))
   print("{:>44s}".format("Good luck and may the force be with you!\n"))
   
def getFuel():
   #ask user
   fuelAmount = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
   #check   
   while fuelAmount <= 0:
      print("ERROR: Amount of fuel must be positive, pleae try again")
      fuelAmount = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
   #loop
   return fuelAmount

def getAltitude():
   altitude = int(input("Enter the initial altitude of the LM (in meters): "))
   while altitude < 1 or altitude > 9999:
      print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
      altitude = int(input("Enter the initial altitude of the LM (in meters): ")) 
   return altitude
  
def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
   #print("\nLM state at retrorocket cutoff")
   print("{:>13s}{:>4d}{:s}".format("Elapsed Time: " ,elapsedTime, " s"))
   print("{:>14s}{:>4d}{:s}".format("Fuel: ", fuelAmount, " l"))
   print("{:>14s}{:>4d}{:s}".format("Rate: ", fuelRate, " l/s"))
   print("{:>14s}{:>7s}{:s}".format("Altitude: ", "%.2f" %altitude,  " m"))
   print("{:>14s}{:>7s}{:s}".format("Velocity: ", "%.2f" % velocity, " m/s\n"))

def getFuelRate(currentFuel):
   #ask for how much fuel they have (currentFuel)
   rate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   while rate < 0 or rate > 9:
      #making sure they input a valid integer
      print("ERROR: Fuel rate must be between 0 and 9, inclusive\n")
      rate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   if rate < currentFuel:
      return rate
   else:
      return currentFuel

def updateAcceleration(gravity, fuelRate):
   acceleration = float(gravity) * ((int(fuelRate) / 5) -1)
   return acceleration

	
def updateAltitude(altitude, velocity, acceleration):
   altitude2 = float(altitude) + float(velocity) + (float(acceleration)/2)
   if altitude <= 0:
      altitude2 = 0
   return altitude2

def updateVelocity(velocity, acceleration):
   velocity2 = float(velocity) + float(acceleration)
   return velocity2

def updateFuel(fuel, fuelRate):
   print(fuel, "    ", fuelRate)
   fuel2 = fuel - fuelRate
   if fuel2 <=0:
      fuel2 = 0
   return fuel2

def displayLMLandingStatus(velocity):
   if velocity <= 0 and velocity >= -1:
      print("Status at landing - The eagle has landed!")
   if velocity <= -1 and velocity >= -10:
      print("Status at landing - Enjoy your oxygen while it lasts!")
   if velocity <= -10:
      print("Status at landing - Ouch - that hurt!")
#altitude, velocity, fuel
