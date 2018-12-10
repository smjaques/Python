#Name:  Sydney Jaques
#Instructor:  Workman

from sys import *
import math

#argv must take 4 command line arguments: name of image file, row, column, fade radius


#the fade center is the x,y coordinates given in argv [3, 4]
def process_pixel(pixel, radius, distance, filewrite):
   #pixel = [r\n, g\n, b\n]
   stripped = []
   for each in pixel:
      if '\n' in each:
         new = each.strip('\n')
         stripped.append(new)

   R = int(stripped[0])
   G = int(stripped[1])
   B = int(stripped[2])

   equation = (radius - distance) / radius
   if equation < .2:
      R = int(R * .2)
      G = int(G * .2)
      B = int(B * .2)
   else:
      R = R * equation
      G = G * equation
      B = B * equation
   
   R = int(R)
   G = int(G)
   B = int(B)

   R = str(R) + '\n'
   G = str(G) + '\n'
   B = str(B) + '\n'

   filewrite.write(R)
   filewrite.write(G)
   filewrite.write(B)



def distance_from_center(x, y, x_center, y_center):
   return math.sqrt((x_center - x)**2 + (y_center - y)**2)



def main():
   if len(argv) != 5:
      return(print('Usage: python3 fade.py <image> <row> <column> <radius>'))
   try: 
      fileread = open(argv[1], 'r')
   except:
      print('Unable to open ' + str(argv[1]))

   filename = str(argv[1])
   fileread = open(filename, 'r')
   filewrite = open('faded.ppm', 'w')
   x_coordinate_center = int(argv[3])
   y_coordinate_center = int(argv[2])
   radius = int(argv[4])
   header_info = []

   for i in range(3):
      header_info.append(fileread.readline())
   filewrite.write(str(header_info[0]))
   filewrite.write(str(header_info[1]))
   filewrite.write(str(header_info[2]))




   width_length = header_info[1].split(' ')
   width = int(width_length[0])
   lenth = int(width_length[1])
# ---- Now get each pixel ----
   pixel = []
   x = 0
   y = 0
   for line in fileread:
      line = line.split(' ')

      for each in line:
         pixel.append(each)
         if len(pixel) == 3:
            coordinate = (x, y)
            distance = distance_from_center(x, y, x_coordinate_center, y_coordinate_center)
            process_pixel(pixel, radius, distance, filewrite)
            y += 1
            if y > width - 1:
               y = 0
               x += 1
            pixel = []
   fileread.close()












if __name__ == '__main__':
   main()
