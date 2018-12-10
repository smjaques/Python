nums = [6, 2, 9, 10]

for num in nums:
   print(num)



for i in range(len(nums)):
   print(nums[i], i)


print('\n')


words = ["hello", "cat", "python", "Wednesday", "WISH"]
#how to find the average length of words ... number of letters divided by number of words you have

#letters:
count = 0
for word in words:
   count += len(word)
   #adds the length of each word to your count
print("Avg len: ", count / len(words))


print('\n')
#how to double a each value in a list in another list
nums = [1, 5, 3, 10]
doubles = []
for x in nums:
   doubles.append(2*x)

print(doubles)
#shortcut for this
print('\n')

doubles2 = [2*x for x in nums]
print(doubles2)
print('\n')

#more complicated form of mapping
def func(n):
   return n **2 - 23*n + 100
vals = [func(x) for x in nums]
#this puts each value from nums into the func equation and returns it in a lista
#map patterns




print('\n')
nums2 = [1, 7, -8, 45, 12, 4, 7, 100]
#we are going to see if each is even
evens = [for x in nums if x%2 == 0]
#this is a filter pattern, won't change x but only copy it into the new list if the if statement is true
#filter pattern 
