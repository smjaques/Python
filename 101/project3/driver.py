from solverFuncs import *

#cages = get_cages()
#puzzle = ([1, 1, 3, 5, 3], 
#          [0, 2, 0, 3, 4], 
#          [4, 5, 0, 7, 8],
#          [3, 4, 5, 8, 7])
#row = [1, 2, 4, 2, 3]
#check_row_valid(row)
#check_rows_valid(puzzle)
#check_columns_valid(puzzle)

#column = ([1, 1, 2, 3, 4], 
#          [0, 2, 3, 4, 5], 
#          [0, 4, 6, 0, 1])
#check_columns_valid(column)

puzzle = [5, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
cages = [9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13], [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16], [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]
#cage = [9, 3, 1, 2, 6]
#cages = [9, 3, 1, 2, 6], [9, 3, 1, 9, 10]
#check_cage_valid(puzzle, cage)
#cages = ([7, 2, 6, 11], [15, 4, 0, 3, 9, 11])
#check_cages_valid(puzzle, cages)
#check_rows_valid(puzzle)
check_valid(puzzle, cages)



