#Sydney Jaques
#Fold


def sum(list1):
   sums = 0
   for i in list1:
      sums += i
   return sums


def index_of_smallest(list1):
   if any(y for y in list1):
      smallest = list1[0]
   for num in list1:
      if num < smallest:
         smallest = num
   for i in range(len(list1)):
      if list1[i] == smallest:
         return i
   return -1




