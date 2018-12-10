#Unittest for SolverFuncs

import unittest
from solverFuncs import *

class TestCases(unittest.TestCase):
      
   def test_check_rows0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertTrue(check_rows_valid(puzzle))
   def test_check_rows1(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 2, 2, 0, 0])
      self.assertFalse(check_rows_valid(puzzle))
   def test_check_rows2(self):
      puzzle = [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
      self.assertTrue(check_rows_valid(puzzle)) 


   def test_check_cols0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 2, 2, 0, 0])
      self.assertFalse(check_columns_valid(puzzle))
   def test_check_col1(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 4, 5, 0, 0])
      self.assertTrue(check_columns_valid(puzzle))
   def test_check_cols2(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 4, 5, 0, 4])
      self.assertFalse(check_columns_valid(puzzle))
   def test_check_cols3(self):
      puzzle = [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
      self.assertTrue(check_columns_valid(puzzle))

   def test_cages(self):
      puzzle = ([1, 1, 3, 5, 3],
                [0, 2, 0, 3, 4],
                [4, 5, 0, 7, 8],
                [3, 4, 5, 8, 7])
      cages = [9, 3, 1, 2, 6], [9, 3, 1, 9, 10]
      self.assertFalse(check_cages_valid(puzzle, cages))
   def test_cages1(self):
      puzzle = ([1, 1, 3, 5, 3],
                [0, 2, 0, 3, 4],
                [4, 5, 0, 7, 8],
                [3, 4, 5, 8, 7])
      cages = [6, 3, 1, 2, 6], [9, 3, 1, 9, 10]
      self.assertTrue(check_cages_valid(puzzle, cages))
   def test_cages2(self):
      puzzle = ([1, 1, 3, 5, 3],
                [0, 2, 0, 3, 4],
                [4, 5, 0, 7, 8],
                [3, 4, 5, 8, 7])
      cages = [6, 3, 1, 2, 6], [5, 3, 2, 8]
      self.assertFalse(check_cages_valid(puzzle, cages))
   def test_cages3(self):
      puzzle = [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
      cages = [8, 2, 0, 1], [15, 5, 0, 5, 10, 15, 20]
      self.assertTrue(check_cages_valid(puzzle, cages))
   def test_cages4(self):
      puzzle = [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
      cages = [9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13], [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16], [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]
      self.assertTrue(check_cages_valid(puzzle, cages))

   def test_valid(self):
      puzzle = ([1, 1, 3, 5, 3],
                [0, 2, 0, 3, 4],
                [4, 5, 0, 7, 8],
                [3, 4, 5, 8, 7])
      cages = [9, 3, 1, 2, 6], [9, 3, 1, 9, 10]
      self.assertFalse(check_cages_valid(puzzle, cages))
   def test_valid2(self):
      puzzle = ([3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [4, 3, 5, 2, 1])
      cages = [9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13], [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16], [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]
      self.assertTrue(check_cages_valid(puzzle, cages))
   def test_valid3(self):
       puzzle = ([3, 5, 2, 1, 4],
                [5, 0, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [4, 0, 5, 2, 1])
       cages = [8, 2, 0, 1], [15, 5, 0, 5, 10, 15, 20]
       self.assertTrue(check_valid(puzzle, cages))
   def test_valid4(self):
      puzzle = ([3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 0, 0, 3, 5],
                [4, 3, 5, 2, 1])
      cages = [8, 2, 0, 1], [15, 5, 0, 5, 10, 15, 20]
      self.assertTrue(check_valid(puzzle, cages))
   def test_valid5(self):
      puzzle = ([3, 5, 2, 1, 4],
                [0, 1, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [4, 3, 5, 2, 1])
      cages = [8, 2, 0, 1], [15, 5, 0, 5, 10, 15, 20]
      self.assertTrue(check_valid(puzzle, cages))
   def test_valid6(self):
      puzzle = [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
      cages = [9, 3, 0, 5, 6], [7, 2, 1, 2], [10, 3, 3, 8, 13], [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16], [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]
      self.assertTrue(check_valid(puzzle, cages))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
