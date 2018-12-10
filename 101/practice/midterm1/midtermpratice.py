#1


cans = 0
people = 0
while cans < 100:
   num = int(input("How many cans? "))
   cans += num
   people += 1

print("Total donations:", people)
print("Total number of cans:", cans)
print("\n")


#2

again = 'y'
while again == 'y':
   print("Hello!")
   again = str(input("Again (y/n)? "))
else:
   print("Goodbye!")
print("\n")


#3

def shape3(size):
   for i in range(size):
      for j in range(size):
         print(i+j, end="")
      print('')

shape3(5)



#4

def check_integer(num):
   if num > 0:
      print('Positive!')
      if num % 2 == 0:
         print('Positively even!')
      else:
         print('Positively odd!')

check_integer(6)



#5
min = int(input("Minimum: "))
max = int(input("Maximum: "))
secret = randint(min, max)

num = int(input('Guess a number between', min, "and", max))
guesses = 1

while num != secret and guesses < 5:
   num = int(input('Nope! Guess again: '))
   guesses += 1
if num == secret:
   print('You win! You made', guesses, "guesses")
else:
   print("You lose!") 
