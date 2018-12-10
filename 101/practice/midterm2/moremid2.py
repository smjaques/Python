#Midterm2 Practice Worksheets

#list of lists
#nums = [[98, 90, 91], [46, 76, 62], [85, 90, 83], [77, 79, 81]]

def sum_row(rows):
   sums = 0
   for num in rows:
      sums += num
   return sums

def sum_2D(nums):
   total = []
   for each in nums:
      s = sum_row(each)
      total.append(s)
   return sum_row(total)


def student_pass(grades, passing = 70):
   passed = []
   for grade in grades:
      if grade >= passing:
         passed.append(True)
      else:
         passed.append(False)
   if all(x == True for x in passed):
      return True
   else:
      return False

def all_passing(grades, passing = 70):
   lists = []
   for each in grades:
      s = student_pass(each)
      lists.append(s)
   return lists



#more list practice with strings
def reverse_word(words):
   new = []
   for i in range(len(words)-1, -1, -1):
      new.append(words[i])
   return ''.join(new)


def alpha_only(strings):
   alphs = []
   for i in strings:
      if i.isalpha() == True:
         alphs.append(i)
   return alphs



def pig_latin(word):
   vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
   if word[0] in vowels:
      return word + 'way'
   else:
      return word[1:] + word[0].lower()  + 'ay'



def contains_at_least_2_vowels(strings):
   vowel_words = []
   for word in strings:
      vowel_count = 0
      for c in word:
         if c in 'aeiouAEIOU':
            vowel_count += 1
            if vowel_count == 2:
               vowel_words.append(word)
   return vowel_words


string = 'hello'
strings = ['hello', 'world']
for i in string:
   print(ord(i))
foo = [1, 2, 3, 4]   
print(chr(97)) #returns the string 'a' because they have the same askew number


sales = [(32, 'Alex', 'Betty', 'Carol'), (17, 'Danna', 'Ellie', 'Fran')]
girl = input('Which girl? ')
for i in sales:
   girls = i[1:]
   if girl in girls:
      print(i[0])

alist = 'asdr'
forbid = 'ezxcvbn'
for i in alist:
   if i in forbid:
      print(False)
print(True)
