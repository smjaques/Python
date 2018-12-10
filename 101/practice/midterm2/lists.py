#February 15
#Lists for Project

nums = [6, 18, 2, -5, 8]
sum = 0
i = 0
while i < len(nums):
   sum += nums[i]
   #adding 6 to sum, then add next index to sum also
   i += 1

#or a for loop
for i in range(len(nums)):
   #I will one at a time take the value of each in range
   sum += nums[i]


#or
for num in nums:
   sum += num
   #here getting the actual item out of the list, instead of the index
   num += 2
   #here you actually change the values in the list

