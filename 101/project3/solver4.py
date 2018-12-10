
#Solver.py
#Name:  Sydney Jaques
#Instructor: Workman

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


while row < len(puzzle):
   while col < len(puzzle):
      print(puzzle)
      puzzle[row][col] += 1
      v = check_valid(puzzle, cages)
      checks += 1
      if v == True:
         col += 1
      if col == 5 and v == True:
         col = 0
         row += 1
      #while loop for backtracks? if false
      if v == False and puzzle[row][col] == 5:
         if col == 0:
            puzzle[row][col] = 0
            col = 4
            row -= 1
            backtracks +=1
         else:
            puzzle[row][col] = 0
            col -=1
            backtracks +=1
            



"""

while row < len(puzzle):
   print(puzzle)
   while col < len(puzzle):
      puzzle[row][col] += 1
      v = check_valid(puzzle, cages)
      checks += 1
      if v == True:
         col += 1
      if col == 5 and row == 4 and v== True:
         row += 1
      if col == 5 and v == True and row != 5:
         col = 0
         row += 1
      if v == False and puzzle[row][col] == 5:
         if col == 0:
            puzzle[row][col] = 0
            col = 4
            row -= 1
         else:
            puzzle[row][col] = 0
            col -= 1
            backtracks += 1



for i in range(len(puzzle)):
   for j in range(len(puzzle)):
      puzzle[row][col] += 1
      v = check_valid(puzzle, cages)
      checks += 1
      if v == True:
         if puzzle[row][col] == 5:
            row += 1
            col = 0
         else:
            col += 1
      if v == False and puzzle[row][col] == 5:
         if col == 0:
            col = 4
         else:
            puzzle[row][col] = 0
            col -= 1
            backtracks += 1
      print(puzzle)

"""

print('\n')
print("--Solution--")
print('\n')

for i in range(5):
   for j in range(5):
      print(puzzle[i][j],'', end = '')
   print('')
      

print('\nchecks: ', checks, "backtracks: ", backtracks)     
print('\n')
