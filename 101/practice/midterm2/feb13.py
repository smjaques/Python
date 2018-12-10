#Splitting of Strings for project

str = '1 2 3'
str.split()
print(str)

#to append something to the list
#(thing I want to append to, what i want to append)
#str.append(4)
#same thing
#for project, would use a list comprehension



print('\n')
#making a function that takes a single character and converts it to uppercase
#you only want to mess with something that is a lowercase character
def char_upper(c):
   if not c.islower():
      return c
   ord_c = ord(c)
   #the difference between uppercase and lowercase is -32
   ord_c -= 32
   return chr(ord_c)
print('\n')

#changing strings (usually immutable)
s = 'hello'
s = list(s)
print(s)
#now s is a list of characters, you can change it
s[1] = 'a'
print(s)
#now join it back together
s1 = ''.join(s)
#take s list, join it back together, and put nothing in between it ('')
print(s1)
s2 = ','.join(s)
print(s2)

#now we can change the string again
print('\n')
def str_upper(s):
   s = "a3Bd"
   res = [char_upper(c) for c in s]
   #map list comprehension
   print(res)
