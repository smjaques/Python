from solverFuncs import *

puzzle = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]
cages = get_cages()
row = 0
col = 0
checks = 0
backtracks = 0

"""
while row < len(puzzle):
   row +=1
   col = 0
   while col < len(puzzle):
      puzzle[row][col] += 1
      v = check_valid(puzzle, cages)
      checks +=1
      while v == False:
         if puzzle[row][col] == 5:
            if col == 0:
               row -=1
               col = 4
               backtracks +=1
            if row != 0 and row <=4:
               puzzle[row][col] = 0
               row -= 1
               backtracks +=1
      if col == 5 and v == True:
         col = 5
"""

while row < 5:
   while col < 5:
      puzzle[row][col] += 1
      check_valid(puzzle, cages)
      checks += 1
      while check_valid(puzzle, cages)  == False:
         print("row", row)
         print("col", col)
         print(puzzle[row][col])
         print(puzzle)
         if puzzle[row][col] < 5:
            puzzle[row][col] +=1
         elif col == 0 and row > 0:
            col = 4
            row -= 1
            backtracks += 1
         elif col > 0:
            col -= 1
            backtracks += 1
         elif col == 0:
            col = 0
      #if col < 4:
      #   col +=1
   col = 0
   row += 1
   #if row < 4:
   #   row +=1

print('\n')
print("--Solution--")
print('\n')

for i in range(5):
   for j in range(5):
      print(puzzle[i][j],'', end = '')
   print('')


print('\nchecks: ', checks, "backtracks: ", backtracks)
print('\n')
