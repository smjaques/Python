#Name:  Sydney Jaques
#Instructor:  Workman

from sys import *

#two demensional list of [[rgb], [rgb], [rgb]]

def get_neighbors(x, y, factor, width, length):
   neighbors_coordinates = []

   x_subtract = 1
   y_subtract = 0
   while x_subtract <= factor:
      y_subtract = 0
      x_subtract += 1

      while y_subtract <= factor:
         point_sub_sub = (x-x_subtract), (y-y_subtract)
         point_sub_add = (x-x_subtract), (y+y_subtract)
         point_add_add = (x+x_subtract), (y+y_subtract)
         point_add_sub = (x+x_subtract), (y-y_subtract)
         neighbors_coordinates.append(point_sub_sub)
         neighbors_coordinates.append(point_sub_add)
         neighbors_coordinates.append(point_add_add)
         neighbors_coordinates.append(point_add_sub)
         y_subtract += 1
   #if any( x < 0 in coordinate in neighbors_coordinates for coordinate in neighbors_coordinates):
    #  neighbors_coordinates.remove(coordinate)
   new = []
   for each in neighbors_coordinates:
      if each[0] >= 0 and each[1] >= 0:
         if each[0] <= width:
            if each[1] <= length:
               new.append(each)
      
   return new



def get_neighbors_pixels(listofpixels, neighbor_coordinates):
   neighbor_pixels = []
   for each_coordinate in neighbor_coordinates:
      for each_pixel in listofpixels:
         if each_coordinate in each_pixel:
            neighbor_pixels.append(each_pixel)

   pixels = []
   for each in neighbor_pixels:
      newlist = []
      newlist.append(each[0])
      newlist.append(each[1])
      newlist.append(each[2])
      pixels.append(newlist)
   return pixels




def average_pixels(neighbor_pixels, factor, length, width):
   sumred = 0
   sumgreen = 0
   sumblue = 0
   for i in range(len(neighbor_pixels)):
      for each in range(len(neighbor_pixels[i])):
         smally = i - factor
         if smally < 0:
            smally = 0
         bigy = i + factor
         if bigy > length:
            bigy = length
         smallx = each - factor
         if smallx < 0:
            smallx = 0
         bigx = factor + each
         if bigx > width:
            bigx = width
   boxes = (bigy - smally) * (bigx - smallx)
   newpixels = []
   for pixel in neighbor_pixels: 
      sumred += int(pixel[0])
      sumgreen += int(pixel[1])
      sumblue += int(pixel[2])
      red = int(sumred / boxes)
      green = int(sumgreen / boxes)
      blue = int(sumgreen / boxes)
      newpixels.append(red)
      newpixels.append(green)
      newpixels.append(blue)
   return newpixels



def main():
#if len(argv) == 1 with my file in it
   if len(argv) == 1 and argv[0] == 'blur.py':
      return(print('Usage: python3 blur.py <image> <OPTIONAL:reach'))
   if len(argv) == 2 :
      argv.append('4')
   try:
      fileread = open(argv[1], 'r')
   except:
      print('Unable to open ' + str(argv[1]))
      exit()

   fileread = open(argv[1], 'r')
   filewrite = open('blurred.ppm', 'w')
   factor = int(argv[2])

# ---- header info ----
   header_info = []

   for i in range(3):
      header_info.append(fileread.readline())
   filewrite.write(str(header_info[0]))
   filewrite.write(str(header_info[1]))
   filewrite.write(str(header_info[2]))


   width_length = header_info[1].split(' ')
   width = int(width_length[0])
   length = int(width_length[1])

# ---- get 2D list of pixels ----
   list_of_pixels = []
   pixel = []
   x = 0
   y = 0
   for line in fileread:
      line = line.split(' ')

      for each in line:
         pixel.append(each)
         if len(pixel) == 3:
            stripped = []
            for each in pixel:
               if '\n' in each:
                  new = each.strip('\n')
                  stripped.append(new)
            coord = []
            coord.append(x)
            coord.append(y)
            coord = tuple(coord)
            stripped.append(coord)
            coord = []
            
            y += 1
            if y > width - 1:
               y = 0
               x += 1
            list_of_pixels.append(stripped)
            pixel = []


# ---- Have list of pixels that looks like this [[R, G, B, X, Y], [R, G, B, X, Y]...] ----

# ---- Get neighbors of each pixel ----

   for pixel in list_of_pixels:
      coordinates = pixel[3]
      x = coordinates[0]
      y = coordinates[1]
      #call function for getting neighbors(x, y, factor)
      neighbor_coordinates = get_neighbors(x, y, factor, width, length)
      print(neighbor_coordinates)
'''
      neighbor_pixels = get_neighbors_pixels(list_of_pixels, neighbor_coordinates)
      average_of_pixels = average_pixels(neighbor_pixels, factor, length, width)
   

      for each in average_of_pixels:
         each = str(each)
         filewrite.write(each + '\n')

   fileread.close()



'''









if __name__ == '__main__':
   main()
