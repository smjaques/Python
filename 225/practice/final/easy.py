#Data definition for a bst

#A Bst is one of 
# - None
# - Node(int, Bst, Bst)
class Node:
    def __init__(self, value, left, right):
        pass

#A bst has a search time of O(logn)



#recusrive calls
def recursion(tree):
    if tree == None:
        return None
    else:
        .....tree.value
        return Node(new_val, recursion(tree.left), recursion(tree.right))




#append strlists
def append(str1, str2):
    if str1 == None:
        return str2
    else:
        return Pair(a.value, append(str1.rest, str2))
