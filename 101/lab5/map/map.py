#Sydney Jaques
#Map

def square_all(list1):
   return[i**2 for i in list1]
   #for i in list1 do function


def add_n_a(n, nums):
   for x in nums:
      return x+n   

def even_or_odd_all(num):
#i = 0
#while(i < len(list1))
   #list1[i] = list1[i]+n
   #saying set the value at the index[i] to the value of index + n
   i = 0
   nums2 = []
   while(i<len(num)):
      if num[i] % 2 == 0:
         nums2.append(True)
      else:
         nums2.append(False)
      i = i + 1
   return nums2
