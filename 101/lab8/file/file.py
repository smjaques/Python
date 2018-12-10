#file.py
#reading from a file



inFile = open("in.txt", "r")

lines = 0
characters = 0


for line in inFile:
   words = line.split()
   characters += len(line)
   print("Line", lines, "("+ str(characters),"chars):", line.strip())
   lines += 1

inFile.close()
      
