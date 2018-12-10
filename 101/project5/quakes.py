#Name:  Sydney Jaques
#Instructor:  Workman
#Quakes.py main


from quakeFuncs import *
from operator import *


filename = "quakes.txt"
earthquakes = read_quakes_from_file(filename)
print('Earthquakes:')
print('------------')
for each in earthquakes:
   formating(each.magnitude, each.place, each.longitude, each.latitude, each.time)

print()
print("Options:\n" + "  (s)ort\n" + "  (f)ilter\n" + "  (n)ew quakes\n" + "  (q)uit")
print()
command = str(input("Choice: "))


while command != 'q' and  command != 'Q':
# ---- filter command ----
   if command == 'f' or command == 'F':
      filter_by = str(input("Filter by (m)agnitude or (p)lace? "))
# ----- filter by place -----
      if filter_by == 'p' or filter_by == "P":
         word = str(input("Search for what string? "))
         filtered = filter_by_place(earthquakes, word)
         print()
         print('Earthquakes:')
         print('------------')
         for each in filtered:
            formating(each.magnitude, each.place, each.longitude, each.latitude, each.time)
# ---- filter by magnitude ----
      if filter_by == 'm' or filter_by == 'M':
         low = float(input("Lower bound: "))
         high = float(input("Upper bound: "))
         filtered = filter_by_mag(earthquakes, low, high)
         print('Earthquakes:')
         print('------------')
         for each in filtered:
            formating(each.magnitude, each.place, each.longitude, each.latitude, each.time)
# ---- sort command ----
   if command == 's' or command == 'S':
      sort = str(input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? "))
# ---- sort by magnitude ----
      if sort == 'm' or sort == 'M':
         earthquakes.sort(key = attrgetter('magnitude'),reverse = True)
         print()
         print('Earthquakes:')
         print('------------')
         for each in earthquakes:
            formating(each.magnitude, each.place, each.longitude, each.latitude, each.time)
# ---- sort by time ----
      if sort == 't' or sort == 'T':
         earthquakes.sort(key = attrgetter('time'), reverse = True)
         print()
         print('Earthquakes:')
         print('------------')
         for each in earthquakes:
            formating(each.magnitude, each.place, each.longitude, each.latitude, each.time)
# ---- sort by longitude ----
      if sort == 'l' or sort == 'L':
         earthquakes.sort(key = attrgetter('longitude'), reverse = True)
         print()
         print('Earthquakes:')
         print('------------')
         for each in earthquakes:
            formating(each.magnitude, each.place, each.longitude, each.latitude, each.time)
# ---- sort by latitude ----
      if sort == 'a' or sort == 'A':
         earthquakes.sort(key = attrgetter('latitude'))
         print()
         print('Earthquakes:')
         print('------------')
         for each in earthquakes:
            formating(each.magnitude, each.place, each.longitude, each.latitude, each.time)
# ---- new quakes command ----
   if command == 'n' or command == 'N':
      url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson'
      newquakes = get_json(url)
      for each in newquakes['features']:
         new = quake_from_feature(each)
# now i need to make sure that i don't have this earthquake in my stuff already
         if new not in earthquakes:
#its not in it so add it to mah list
            earthquakes.append(new)

         print()
         print('New quakes found!!!')
         print()
         print('Earthquakes:')
         print('------------')
         for each in earthquakes:
            formating(each.magnitude, each.place, each.longitude, each.latitude, each.time)
      else:
         print()
         print('Earthquakes:')
         print('------------')
         for each in earthquakes:
            formating(each.magnitude, each.place, each.longitude, each.latitude, each.time)

# ---- options ----
   print()
   print("Options:\n" + "  (s)ort\n" + "  (f)ilter\n" + "  (n)ew quakes\n" + "  (q)uit")
   print()
   command = str(input("Choice: "))


# ---- writing to program when quitting ----



writing_back_to_file(earthquakes, filename)


