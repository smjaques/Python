#Sydney Jaques
#Poly
def poly_add2(list1, list2):
   sum = []
   for i in range(3):
      sum.append(list1[i] + list2[i])
   return sum
   
   
def poly_mult2(first, second):
   list3 = []
   mult = []
   for i in first:
      for j in second:
         mult.append(i * j)
         #variable name, what to pull from; use variable throughout rest of loop
   list3.append(mult[0])
   list3.append(mult[1]+mult[3])
   list3.append(mult[2] + mult[4] + mult[6])
   list3.append(mult[5] + mult[7])
   list3.append(mult[8])
   return list3

