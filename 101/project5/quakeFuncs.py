from urllib.request import *
from json import *
from datetime import *
from operator import *


# GIVEN FUNCTIONS:
# Use these two as-is and do not change them
def get_json(url):
   ''' Function to get a json dictionary from a website.
       url - a string'''
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def time_to_str(time):
   ''' Converts integer seconds since epoch to a string.
       time - an int '''
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')    
   
# Add Earthquake class definition here   
class Earthquake:
   def __init__(self, place, magnitude, longitude, latitude, time):
      self.magnitude = magnitude
      self.time = time
      self.longitude = longitude
      self.latitude = latitude
      self.place = place
   def __eq__(self, other):
      return (self.magnitude == other.magnitude and \
             self.time == other.time and \
             self.longitude == other.longitude and \
             self.latitude == other.latitude and \
             self.place == other.place)
 
   def __repr__(self):
      return 'Earthquake({}, {}, {}, {}, {})'.format(self.place, self.magnitude, self.longitude, self.latitude, self.time)


# Required function - implement me!   
def read_quakes_from_file(filename):
   filename = str(filename)
   inFile = open(filename, "r")
   quakes = []
   for each in inFile:
      new = each.rstrip().split()
      magnitude = float(new[0])
      longitude = float(new[1])
      latitude = float(new[2])
      time = int(new[3])
      place = str(' '.join(new[4:]))
      quakes.append(Earthquake(place, magnitude, longitude, latitude, time))
   inFile.close()
   return quakes



# Required function - implement me!
def filter_by_mag(quakes, low, high):
   sortedq = []
   quakes = list(quakes)
   for quake in quakes:
      if quake.magnitude >= low and quake.magnitude <= high:
         sortedq.append(quake)
   return sortedq


# Required function - implement me!
def filter_by_place(quakes, word):   
   quakes = list(quakes)
   filtered = []
   for each in quakes:
      if word.lower() in each.place.lower():
         filtered.append(each)
   return filtered

# Required function for final part - implement me too!   
def quake_from_feature(feature):
   place = feature['properties']['place']
   magnitude = feature['properties']['mag']
   time = int(feature['properties']['time'] / 1000)
   longitude = feature['geometry']['coordinates'][0]
   latitude = feature['geometry']['coordinates'][1]
   quakes = Earthquake(place, magnitude, longitude, latitude, time)
   return quakes

     
def writing_back_to_file(earthquakes, filename):
   outFile = open(filename, "w")
   #now write it to the file
   for each in earthquakes:
      each.time = int(each.time)
      outFile.write('{} {} {} {} {}\n'.format(each.magnitude,  each.longitude, each.latitude, each.time, each.place))
   #now it's in the file, return the file
   return filename


def formating(magnitude, place, longitude, latitude, time):
   print('({:.2f}){:>40s} at '.format(magnitude, place) + time_to_str(time) + ' ' + '({:8.3f},{:7.3f})'.format(longitude, latitude))




