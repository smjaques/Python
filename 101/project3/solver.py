
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
while row < 5:
   puzzle[row][col] += 1
   check_valid(puzzle, cages)
   checks += 1
   if check_valid(puzzle, cages) == True:
      col += 1
      if col ==5:
         col = 0
         row += 1
   else:
      while puzzle[row][col] ==5:
         puzzle[row][col] = 0
         col -= 1
         if col == -1:
            col = 4
            row -= 1
         backtracks += 1

print("\n---Solution---")
print()

for i in range(5):
   for j in range(5):
      print(puzzle[i][j],'', end = '')
   print('')


print('\nchecks:', checks, "backtracks:", backtracks)
