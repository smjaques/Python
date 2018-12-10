



nums = [5, 3, -2, 7]
def in_func(nums, x):
   for num in nums:
      #goes through every value in nums
      if x == num:
      #x is the number we are looking for
         return True
      #don't want to have else: return False. 
   #but don't forget to have a line that returns False if x isn't in the list
   return False  

#want to give the index of where that number occurs in the list
#if it doesn't occur, return -1
#-1 is because that is usually in invalid index --> indicates it's not there
def index_of(nums, x):
   #need to keep track of the index
   for i in range(len(nums)):
   #i is getting values [0, 1, 2, 3]
   #now need to index into list and see if it's a match of what searching for
      if nums[i] == x:
         return i
   return -1
   #there wasn't a value that == x in the list, so return index -1


#want to get in a list, and want the smallest thing in the list
def smallest(nums):
   #tell us the value of the smallest thing in the list
   small = nums[0] #set to first thing in list, check if there is smaller thing
   for num in nums[1:]:
      if num < small:
         small = num
   return small







