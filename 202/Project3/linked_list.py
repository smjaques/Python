# AnyList is one of the following
# - None
# - Pair(first, rest)

class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest
    def __repr__(self):
        return "Pair(%r, %r)" % (self.first, self.rest)
    def __eq__(self, other):
        return type(other) == Pair and self.first == other.first and self.rest == other.rest

# -> None
# to return an empty list
def empty_list():
    return None

# AnyList int, int, number (any type) -> AnyList
# to place a given value at an given index
def add(anylist, index, value):
    if anylist == None:
        if index == 0:
            return Pair(value, None)
        else:
            raise IndexError
    else:
        if index == 0:
            return Pair(value, anylist)
    return Pair(anylist.first, add(anylist.rest, index - 1, value))

# AnyList -> int
# to determing the length of a list
def length(anylist):
    if anylist == None:
        return 0
    return 1 + length(anylist.rest)

# Anylist, int -> int
# to determine the value at a specific index
def get(anylist, index):
    if index < 0 or anylist == None:
        raise IndexError
    if index == 0:
        return anylist.first
    index -= 1
    return get(anylist.rest, index)

# AnyList, int, int -> AnyList
# to replace a specific index in a list with a specific value
def set(anylist, index, value):
    if index < 0 or anylist == None:
        raise IndexError
    if index == 0:
        return Pair(value, anylist.rest)
    index -= 1
    return Pair(anylist.first, set(anylist.rest, index, value))

# AnyList, int -> 2-tuple
# to remove a value from a list at a specific index and return a new list
def remove(anylist, index):
    if index < 0 or anylist == None:
        raise IndexError
    if index == 0:
        return (anylist.first, anylist.rest)
    index -= 1
    temp = remove(anylist.rest, index)
    return (temp[0], Pair(anylist.first, temp[1]))


#Anylist(sorted) value func --> Anylist
#adds the value in the correct place based on the function, returns the new list
def insert_sorted(alist, value, fn):
    if alist == None:
        return Pair(value, None)
    else:
        if fn(alist.first, value):
            return Pair(alist.first, insert_sorted(alist.rest, value, fn))
        else:
            return Pair(value, alist)





