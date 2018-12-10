#Sydney Jaques
#Instructor:  Workman

#wordFinder

from funcs import *

characters = input()
puzzle = trans_puzzle(characters)
print('Puzzle:')
print()

print_puzzle(puzzle)
print()

words = get_words()
x = 0
for word in words:
   solution = search_puzzle(puzzle, word)
   if solution != None:
      print(str(word) + ':', solution[0], 'row:', solution[1], 'column:', solution[2])
   else:
      print(str(word) + ':', 'word not found')


