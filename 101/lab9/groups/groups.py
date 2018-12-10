#groups.py



def groups_of_3(values):
   n = 3
   return [values[i:i+n] for i in range(0, len(values), n)]
