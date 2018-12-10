#Sorting other ways

def swap(list, i, j):
#giving it a list, and two indices
   temp = list[i]
   list[i] = list[j] #overriding what is in spot i
   list[j] = temp
#the number of passes it will do is n-1
