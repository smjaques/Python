#How to read from a file



inFile = open("stuff.txt", "r")

for line in inFile:
   print(line.strip())
