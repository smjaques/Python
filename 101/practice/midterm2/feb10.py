#list splicing

nums = [1, 5, 2, 10]
print(nums)
print(nums[2:4])
print(nums[:2])


#making a copy of the list
nums2 = nums[:]
print(nums)
print('\n')

#slicing strings like list
str = 'banana'
str[2:5] #would give you 'nan'

#sling a list of strings
words = ['banana', 'hi', 'cat', 'student', 'thing']
words[1:3] #gives you ['hi', 'cat']
words[3][:3] #would give you 'stu'

