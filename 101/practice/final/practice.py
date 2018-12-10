
def have_same_values(ints):
   one = ints[0]
   two = ints[1]
   for x in one:
      if x in two:
         return True
   return False


def avoids(word, forbidden):
   for each in word:
      if each in forbidden:
         return False
   return True


def isInOrder(floats):
   inorder = True
   for i in range(len(floats) - 1):
      if floats[i] > floats[i+1]:
         return False
   return True

def remove_dups(word):
   no_dups = []
   for each in word:
      if each not in no_dups:
         no_dups.append(each)
   new = ''.join(no_dups)
   return new

def deans_list(students):
   deans = []
   for i in range(len(students)):
      all_a = True
      for grade in students[i]:
         if grade != 'A':
            all_a = False
      if all_a == True:
         deans.append(i)
   return deans



def total_distance(route, distance):
   sums = 0
   for i in range(len(route) -1):
      city1 = route[i]
      city2 = route[i+1]
      for each in distance:
         if city1 in each and city2 in each:
            sums += each[2]
   return sums



def program():
   nums = input("Give me two numbers: ")
   nums = nums.split()
   for i in range(len(nums)):
      return int(nums[i]) * int(nums[i+1])
   print(y)

dict = {

   'name': 'Juan',
   'phone': '503-1234',
}

dict2 = {
   'name': 'Alex',
   'phone': '123-4567',
   'adresses': [
      'Home',
      'Work',
      'School',
   ]
}
      

def line_counts(lines, character):
   count = []
   for each in lines:
      how_many = 0
      for one in each:
         if one == character:
            how_many+= 1
      count.append(how_many)
   return count

def sum_lists(list1):
   sums = 0
   for i in range(len(list1)):
      try:
         sums += list1[i]
      except TypeError:
         return 'Error: index' + str(i)
   return sums


def disemvowel(word, y_vowel):
   if y_vowel == True:
      vowels = 'AEIOUYaeiouy'
   else:
      vowels = 'AEIOUaeiou'
   new = []
   for each in word:
      if each not in vowels:
         new.append(each)
   n = ''.join(new)
   return n

def disemvowel_list(list1, y_vowel):
   new = []
   for each in list1:
      y = disemvowel(each, y_vowel)
      new.append(y)
   return new

def findRepeat(word):
   for i in range(len(word)-1):
      if word[i] == word[i+1]:
         return(word[i], i)
   return None

def numbers(string):
   nums = []
   exceptions = []
   s = string.split()
   for i in range(len(s)):
      try:
         number = int(s[i])
         nums.append(number)
      except:
         exceptions.append(i)
   return (nums, exceptions)





