#reading from a file

from sys import *



try:
   inFile = open(argv[1], 'r')
except IndexError: #if something bad happens during try stage
   print("usage: python3 file.py filename")
   exit() #if something bad happened, it will show message, and exit cleanly
   #argv = arguement vector (aka lists)
   #argv[0] = name of program
   #argv[1] = file you want to open
   #errors are called exception (no file, file doesn't exist, wrong permissions)
except IOError as e:
   #means if you catch an IOError exception, give that the variable e
   print(e)
   exit()


#printing each line in a file AKA the MORE FUNCTION
for line in inFile:
   print(line.strip())
   #.strip() gets rid of the empty space before and after each line

