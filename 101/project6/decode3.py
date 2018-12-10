#Name:  Sydney Jaques
#Instructor:  Workman
#Decode.py


#make sure correct file is given
#if so, put it in list of lists
#process one pixel at a time, and write that out to the new image (output)

from sys import *

def is_filename_correct(thing):
   if len(argv) != 2:
      print('Usage: python decode.py <image>')
   try:
      inFile = open(argv[1], 'r')
   except IOError or OSError:
      print('Unable to open' + str(argv[1]))



def processing_pixel(fileread, filewrite):
   #file.readline() reads a single line and moves the cursor to the next one
   header_info = []
   
   for i in range(3):
      header_info.append(fileread.readline())
   filewrite.write(str(header_info[0]))
   filewrite.write(str(header_info[1]))
   filewrite.write(str(header_info[2]))
   R = 1
   while R != '':
      R = fileread.readline()
      if R == '':
         fileread.close()
         exit()
      G = fileread.readline()
      B = fileread.readline()
      R = int(R) * 10
      if R > 255:
         R = 255
      R = str(R) + '\n'
      G = str(R)
      B = str(R)
      #output the pixel
      filewrite.write(R)
      filewrite.write(G)
      filewrite.write(B)
      


'''
header_info = []
for i in range(10):
   my_ln = f.readline()
   if i <= 3:
      header_info.append(i)
   else:
      print(my_ln)
'''   

def main():
   filename = 'puzzle.ppm'
   inFile = open(filename, 'r')
   filewrite = open('decoded.ppm','w')
   processing_pixel(inFile, filewrite)












if __name__ == '__main__':
   main()


   


