#parse file

from sys import *

def is_float(thing):
   try:
      floaty = float(thing)
      return True
   except ValueError:
      return False


def main():
   if len(argv) < 2 or len(argv) > 3:
      return(print('Usage: [-s] file_name'))
   elif len(argv) == 3:
      if '-s' not in argv:
         return(print('Usage: [-s] file_name'))
      elif argv[1] != '-s' and argv[2] != '-s':
         return(print('Usage: [-s] file_name'))
   elif 'text1.txt' not in argv:
      return(print('Unable to open ' + str(argv[1])))



   text = open('text1.txt', 'r')
   integers = 0
   floats = 0
   strings = 0
   summed = 0

   for line in text.readlines():
      things = line.split()
      for thing in things:
         if thing.isdigit() == True:
            integers += 1
            summed += int(thing)
         elif is_float(thing) == True:
            floats += 1
            summed += float(thing)
         else:
            strings += 1


   print('Ints: '+ str(integers))
   print('Floats: '+ str(floats))
   print('Other: ' + str(strings))

   if '-s' in argv:
      print('Sum: ' + str(summed))

   text.close()


if __name__ == '__main__':
   main()
