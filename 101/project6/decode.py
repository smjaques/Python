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



def processing_pixel(pixel, filewrite):
   #file.readline() reads a single line and moves the cursor to the next one
   R = int(pixel[0])
   R = R * 10
   if R > 255:
      R = 255
   R = str(R) + '\n'
   G = R
   B = R
   #output the pixel

   filewrite.write(R)
   filewrite.write(G)
   filewrite.write(B)





def main():
# ---- error messages ----
   if len(argv) < 2 or len(argv) > 3:
      return(print('Usage: python3 decode.py <image>'))
   try:
      fileread = open(argv[1], 'r')
   except:
      print('Unable to open ' + str(argv[1]))
      exit()

   filename = str(argv[1])
   fileread = open(filename, 'r')
   filewrite = open('decoded.ppm','w')

   header_info = []

   for i in range(3):
      header_info.append(fileread.readline())
   filewrite.write(str(header_info[0]))
   filewrite.write(str(header_info[1]))
   filewrite.write(str(header_info[2]))

# ---- Now get each pixel ----
   pixel = []
   for line in fileread:
      line = line.split(' ')
   
      for each in line:
         pixel.append(each)
         if len(pixel) == 3:
            processing_pixel(pixel, filewrite)
            pixel = []
   fileread.close()
   #processing_pixel(fileread, filewrite)












if __name__ == '__main__':
   main()


   


