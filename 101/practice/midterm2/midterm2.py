#Sydney Jaques
#Midterm 2 Practice

list1 = ([1, 2, 3, 4], [5, 6, 7, 8])
#particular spots in a list of lists
print(list1[1][1])
#it's 6... so list[whatever is in spot 1 in list 1]

#adding
add = [1, 2, 3, 4]
add = add + [5]
print(add)

#inserting
n = [1, 3, 4, 5]
n.insert(1, 2)
print(n)


#removing
r = [1, 2, 3, 300, 4, 5]
r.remove(300)
print(r)

#pop
p = [1, 2, 300, 3, 4, 5]
print(p.pop(2))

#check in list
nums = [3, 6, 334, 654, 23, 16, 886]
print(5 in nums)
print(654 in nums)

#to remove all of a value in a list
remove = [1, 300, 2, 3, 300, 4, 300, 5]
while 300 in remove:
   remove.remove(300)
print(remove)

#multiplying a list
m = [1, 2, 3]
m = m * 3
print(m)

#copying a list - the differences
c = [1, 2, 3]
var = c #just has two names for the same list
copy = list(c) #makes a new list out of the values of c
print(copy)
#changing one won't change the other

#tuples, used to return two things from a function
a = 10
b = 4
print(a//b, a%b)

#indexes and lists
num = [45, 2, 12, 6, 78, 4]
for i in range(len(num)):
   print(num[i], i)
   #prints num at spot i and also print the index
   # i is the index, num[i] is the value 

foo = [1, 2, 3, 4, 5]
bar = [2*x for x in foo]
print(bar)

#making function that takes a single character and converts to uppercase
c = 'l'
#if not c.islower(), return c
ord_c = ord(c)
ord_c -= 32
print(chr(ord_c))

#changing strings
s = 'hello'
s = list(s)
#now we can change s!
translation = []
for let in range(len(s)):
   if s[let] == 'l':
      translation.append('p')
   else:
      translation.append(s[let])

print(''.join(translation))



