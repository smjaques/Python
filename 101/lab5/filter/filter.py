#Sydney Jaques
#Filter 

def are_positive(list1):
   list2 = []
   for i in range(len(list1)):
      if(list1[i] > 0):
         list2.append(list1[i])
   return list2


def are_greater_than_n(nums, n):
   list2 = []
   i = 0
   while(i < len(nums)):
      if(nums[i] > n):
         list2.append(nums[i])
      i += 1
   return list2


def are_divisible_by_n(list1, n):
   return [list1[x] for x in range(len(list1)) if list1[x] %n == 0]

