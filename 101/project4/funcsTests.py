#Sydney Jaques
#funcsTests

import unittest
from funcs import *


class TestCases(unittest.TestCase):

   def test_trans(self):
      characters = 'WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'
      self.assertEqual(trans_puzzle(characters), ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU'])
   def test_trans2(self):
      characters = 'EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR'
      self.assertEqual(trans_puzzle(characters), ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR'])


   def test_searchrow(self):
      word = 'cat'
      row = 'anskcatnsj'
      self.assertEqual(search_row(row, word), 4)
   def test_searchrow2(self):
      word = 'meow'
      row = 'asdcrwobjk'
      self.assertEqual(search_row(row, word), None)

   def test_searchrows(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'UNIX'
      self.assertEqual(search_rows(puzzle, word), [9, 3])
   def test_searchrows2(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'UNId'
      self.assertEqual(search_rows(puzzle, word), [])

   def test_searchcolumns(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'CALPOLY'
      self.assertEqual(search_columns(puzzle, word), [1, 0])
   def test_searchcolumns2(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'mike'
      self.assertEqual(search_columns(puzzle, word), [])

   def test_searchrbackwards(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'VIM'
      self.assertEqual(search_rows_backwards(puzzle, word), [1, 4])
   def test_searchrbackwards2(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'my'
      self.assertEqual(search_rows_backwards(puzzle, word), [])
   def test_searchrbackwards3(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'QAW'
      self.assertEqual(search_rows_backwards(puzzle, word), [0, 2])

   def test_searchcbackwards(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'COMPILE'
      self.assertEqual(search_cols_backwards(puzzle, word), [6, 8])
   def test_searchcbackwards2(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'mike'
      self.assertEqual(search_cols_backwards(puzzle, word), [])     
   def test_searchbackwards3(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'UZM'
      self.assertEqual(search_cols_backwards(puzzle, word), [9, 9]) 


   def test_searchpuzzle(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'CALPOLY'
      self.assertEqual(search_puzzle(puzzle, word), ['(DOWN)', 1, 0])
   def test_searchpuzzle1(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'sydney'
      self.assertEqual(search_puzzle(puzzle, word), None)
   def test_searchpuzzle2(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'UNF'
      self.assertEqual(search_puzzle(puzzle, word), ['(BACKWARD)', 9, 9])
   def test_searchpuzzle3(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'WAQ'
      self.assertEqual(search_puzzle(puzzle, word), ['(FORWARD)', 0, 0])
   def test_searchpuzzle4(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'UNIX'
      self.assertEqual(search_puzzle(puzzle, word), ['(FORWARD)', 9, 3])
   def test_searchpuzzle5(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'GCC'
      self.assertEqual(search_puzzle(puzzle, word), None)
   def test_searchpuzzle6(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'SLO'
      self.assertEqual(search_puzzle(puzzle, word), ['(FORWARD)', 7, 2])
   def test_searchpuzzle7(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'COMPILE'
      self.assertEqual(search_puzzle(puzzle, word), ['(UP)', 6, 8])
   def test_searchpuzzle8(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'VIM'
      self.assertEqual(search_puzzle(puzzle, word), ['(BACKWARD)', 1, 4])
   def test_searchpuzzle9(self):
      puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
      word = 'TEST'
      self.assertEqual(search_puzzle(puzzle, word), None)






if __name__ == '__main__':
   unittest.main()
