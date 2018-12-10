#Sydney Jaques
#Strspn.py

def main():
   str1 = input('Enter string1: ')
   str2 = input('Enter string2: ')
   result = my_strspn(str1, str2)
   print('Result: ', result)

def my_strspn(str1, str2):
   dups = []
   for each in str1:
      if each in str2:
         dups.append(each)
      else:
         return len(dups)
   return len(dups)


if __name__ == "__main__":
   main()
