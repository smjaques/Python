#just a driver
from funcs import *


characters = 'EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR'
print(trans_puzzle(characters))
puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'AZXWKWIIIL', 'LDWLFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']

#print(trans_puzzle(characters))
words = ['UNIX', 'CALPOLY',  'GCC',  'SLO', 'COMPILE', 'VIM', 'TEST']

word = 'CALPOLY'

#print(search_rows(puzzle, word))
#print(search_columns(puzzle, word))
#print(search_rows_backwards(puzzle, word))
#print(search_cols_backwards(puzzle, word))
print(search_puzzle(puzzle, word))







