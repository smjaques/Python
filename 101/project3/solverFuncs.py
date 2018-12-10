
#Name: Sydney Jaques
#Instructor: Workman
#Section: 05


def get_cages():
   cages = int(input("Number of cages: "))
   x = 0
   list1 = []
   lists= []
   while x < cages:
      print("Cage number", x, end = '')
      input1 = input(': ')
      input1 = input1.split()
      list1 = []
      for i in input1:
         input1 = int(i)
         list1.append(input1)
      lists.append(list1)
      x += 1
   return lists
   
   

def check_row_valid(puzzle):
   x = 1
   list = []
   while x < 6:
      count = puzzle.count(x)
      x += 1
      list.append(count)
   if all(i < 2 for i in list):
      return True 
   else:
      return False

  
def check_rows_valid(puzzle):
   list1 = []
   for i in puzzle:
      x = (check_row_valid(i))
      list1.append(x)
   if all(y == True for y in list1):
      return True
   else:
      return False



def check_valid(puzzle, cages):
   valid = []
   rows = check_rows_valid(puzzle)
   valid.append(rows)
   cols = check_columns_valid(puzzle)
   valid.append(cols)
   cages = check_cages_valid(puzzle, cages)
   valid.append(cages)
   if all(y == True for y in valid):
      return True
   else:
      return False 

def check_cage_valid(puzzle, cage):
   total = (cage[0])
   nums = (cage[1])
   cells = (cage[2:])
   add = 0
   comp = True
   for i in cells:
      row = i//5
      col = i%5
      add += puzzle[row][col]
      if puzzle[row][col] == 0:
         comp = False
   if comp == False and add >= total:
      return False
   if comp == True and add != total:
      return False
   else:
      return True
#need variable to see if comp: True or False
#conver to get value out of each spot in cells
#add value to add
#if value at that spot == 0: set complete to false

#invalid if it is complete and doesn't equal the total
#invalid if incomplete and it is >= total

   #if any(puzzle[i//5][y%5] == 0 for y in cells) and add <= total:
   #   return True
   #if any(puzzle[i//5][i%5] !=0 for y in cells) and add == total:
   #   return True
#   if any(y == 0 for y in cells) and add <= total:
#      return True
#   if any(y != 0 for y in cells) and add == total:
#      return True
#   else:
#      return False

#if cage is incomplete, if sum is less than total -> true
#if cage is complete and sum isn't total -> false
#if cage is incomplete and sum isn't total -> true
#keep track whether it's complete or not
def check_cages_valid(puzzle, cages):
   list = []
   for i in cages:
      valid = check_cage_valid(puzzle, i)
      list.append(valid)
   if all(y == True for y in list):
      return True
   else:
      return False

def check_columns_valid(puzzle):
   cols = []
   valid = []
   y = 0
   for i in puzzle:
      x = (i[y])
      cols.append(x)
   v = check_row_valid(cols)
   y = 1
   valid.append(v)
   cols = []
   for i in puzzle:
      x = (i[y])
      cols.append(x)
   v = check_row_valid(cols)
   valid.append(v)
   y = 2
   cols = []
   for i in puzzle:
      x = (i[y])
      cols.append(x)
   v = check_row_valid(cols)
   valid.append(v)
   y = 3
   cols = []
   for i in puzzle:
      x = (i[y])
      cols.append(x)
   v = check_row_valid(cols)
   valid.append(v)
   y = 4
   cols = []
   for i in puzzle:
      x = (i[y])
      cols.append(x)
   v = check_row_valid(cols)
   valid.append(v)

   if all(y == True for y in valid):
      return True
   else:
      return False
#l[0][0] to check first place in first list
