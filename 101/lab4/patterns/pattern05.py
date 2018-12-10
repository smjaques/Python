#Pattern05

import driver

def letter(row, col):
   if row == col or row < col:
      return 'W'
   else:
      return 'T'





if __name__ == '__main__':
   driver.comparePatterns(letter)
