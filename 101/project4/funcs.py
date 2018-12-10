#Sydney Jaques
#Project 4 - Word Search
#Instructor - Workman



def trans_puzzle(characters):
   puzzle = []
   row0 = []
   row1 = []
   row2 = []
   row3 = []
   row4 = []
   row5 = []
   row6 = []
   row7 = []
   row8 = []
   row9 = []
   for i in range(10):
      row0.append(characters[i])
   for i in range(10, 20):
      row1.append(characters[i])
   for i in range(20, 30):
      row2.append(characters[i])
   for i in range(30, 40):
      row3.append(characters[i])
   for i in range(40, 50):
      row4.append(characters[i])
   for i in range(50, 60):
      row5.append(characters[i])
   for i in range(60, 70):
      row6.append(characters[i])
   for i in range(70, 80):
      row7.append(characters[i])
   for i in range(80, 90):
      row8.append(characters[i])
   for i in range(90, 100):
      row9.append(characters[i])
   puzzle.append(row0)
   puzzle.append(row1)
   puzzle.append(row2)
   puzzle.append(row3)
   puzzle.append(row4)
   puzzle.append(row5)
   puzzle.append(row6)
   puzzle.append(row7)
   puzzle.append(row8)
   puzzle.append(row9)
   final = []
   for each in puzzle:
      joined = ''.join(each)
      final.append(joined)
   return final


def print_puzzle(puzzle):
   for each in puzzle:
      if each != None:
         print(each)
#how to print the puzzle look: for each in puzzle: print each


def get_words():
   words = str(input())
   words = words.split()
   return words
   #split = []
   #word = []
   #for each in words:
   #   word.append(each)
   #split.append(word)
   #return split


def solutions(found):
   solutions = []
   return solutions.append(found)


def search_row(row, word):
   #row = [WAGHGTTWEE]
   #word = slo
   if word in row:
      return row.find(word)


def search_rows(puzzle, word):
   count = -1
   index = []
   for row in puzzle:
      found = search_row(row, word)
      count += 1
      if found != None:
         index.append(count)
         index.append(found)
   return index
   


"""
def not_in_puzzle(stuff):
   nones = []
   for i in stuff:
      if i[1]== None:
         nones.append(i[0])
   seen_twice = set([x for x in nones if nones.count(x) > 1])
   not_found = list(seen_twice)
   return not_found
"""


def search_columns(puzzle, word):
   new = list(zip(*puzzle))
   newcols = []
   for each in new:
      check = ''.join(each)
      newcols.append(check)
   stuff = search_rows(newcols, word)
   return stuff[::-1]


#      new = zip(*each)
#      newpuz.append(new)
#   return newpuz
   #stuff = search_rows(new, words)
   #return stuff
   



def search_rows_backwards(puzzle, word):
   word  = word[::-1]
   found = search_rows(puzzle, word)
   if found:
      found[1] = found[1] + len(word) - 1
      return found
   return found


def search_cols_backwards(puzzle, word):
   new = word[::-1]
   found = search_columns(puzzle, new)
   if found:
      found[0] = found[0] + len(new) - 1
      return found
   return found


def search_puzzle(puzzle, word):
   rows = search_rows(puzzle, word)
   if rows:
      answer = ['(FORWARD)', rows[0], rows[1]]
      return answer
   cols = search_columns(puzzle, word)
   if cols:
      columns = ['(DOWN)', cols[0], cols[1]]
      return columns
   backwards = search_rows_backwards(puzzle, word)
   if backwards:
      back = ['(BACKWARD)', backwards[0], backwards[1]]
      return back
   up = search_cols_backwards(puzzle, word)
   if up:
      ups = ['(UP)', up[0], up[1]]
      return ups
   return None

