#Sydney Jaques
#Conditional.py

def max_101(s, j):
   if s < j:
      return j
   elif j < s:
      return s
   elif j == s:
      return j

def max_of_three (a, b, c):
   if a > b > c:
      return a
   elif b > c > a:
      return b
   elif a > c > b:
      return a
   elif b > a > c:
      return b
   elif c > b > a:
      return c
   elif c > a > b:
      return c
   elif a >= b > c:
      return a
   elif a >= c > b:
      return a
   elif b >= a > c:
      return b
   elif b >= c > a:
      return b
   elif c >= b > a:
      return c
   elif c >= a > b:
      return c

def rental_late_fee(d):
   if d <= 0:
      return 0
   elif 0 < d <= 9:
      return 5
   elif 9 < d <= 15:
      return 7
   elif 15 < d <= 24:
      return 19
   elif 24 < d:
      return 100












