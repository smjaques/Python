
#While Loops. We know in advance how many times to run it = ForLoop


x = 10
while x > 0:
   print(x, '...')
   x = x - 1
print("Blast off!")


print("\n")
#More While Loops
print("\nWhile loops continued")
answer = 'y'
while answer == 'y' or answer == "Y":
   print("Hello!")
   answer = input("Again (y/n)? ")
   while answer != 'y' and answer != 'n':
      answer = input("Enter y or n! ")
print("Goodbye!")

#We want to change it so that if anything other than n is typed, Hello is still printed
   #while answer != 'n' and answer !='N':



print('\n')
#While Loops until condition is met
print("\n")
total = 0
while total < 100:
   num = int(input("Num: "))
   total += num
print("Final total:", total)
   


#forLoops
print('\n')
print('\n')
list = [1, 2, 3, 4, 5]
for num in list:
   print(num)

#range(3) --> makes list [0, 1, 2] (doesn't include 3)

