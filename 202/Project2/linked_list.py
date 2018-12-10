#from linked_list_lab import *

#A linkedlist is one of
# - None
# - Catalog(int, str, str, str, linkedlist)
class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest
    def __repr__(self):
        return 'Pair({}, {})'.format(self.first, self.rest)
    def __eq__(self, other):
        return (type(other) == Pair and self.first == other.first and self.rest == other.rest)


def length(alist):
    if alist == None:
        return 0
    else:
        return 1 + length(alist.rest)



#anylist, func -->
# in order to keep your place when you run a function inside a loop
def foreach(list, order, func):
    if list !=None:
        func(list.first, order)
        order += 1
        foreach(list.rest, order, func)


def insertion_sort(func, value, sorted_list):
    if sorted_list == None:
        return Pair(value, None)
    else:
        if not func(value, sorted_list.first):
        #value, sorted_list.first)
            #return Pair(insertion_sort(func, value, sorted_list.rest), sorted_list.first)
            return Pair(sorted_list.first, insertion_sort(func, value, sorted_list.rest))
        else:
            return Pair(value, Pair(sorted_list.first, sorted_list.rest))


def sort(alist, func):
    sorted_list = empty_list()
    while alist != None:
        sorted_list = insertion_sort(func, alist.first, sorted_list)
        alist = alist.rest
    return sorted_list



# --> empty list 
#takes no arguments and returns an empty list
def empty_list():
    return None

#An index is an int representing the position of an element
#anylist index value --> places the value at index position in the list

def add(anylist, index, value):
    if index < 0 or index > length(anylist):
        raise IndexError
    if anylist == None:
        return Pair(value, None)
    else:
        if index == 0:
            return Pair(value, anylist)
        else:
            return Pair(anylist.first, add(anylist.rest, index-1, value))



#anylist index --> int
#returns the value of the index position at the index
def get(anylist, index):
    #if int(index) < 0:
    #    raise IndexError
    if anylist == None:
        raise IndexError
    if int(index) == 0:
        return anylist.first
    return get(anylist.rest, int(index)-1)


#anylist index value --> list
#returns new list with element at the index position replaced with the value given
def set(anylist, index, value, current_index=0):
    if index < 0 or index > length(anylist):
        raise IndexError
    else:
        if current_index == index:
            return Pair(value, anylist.rest)
        else:
            current_index += 1
            return Pair(anylist.first, set(anylist.rest, index, value, current_index))

#AnyLIst, int --> tuple
#to remove a value from a list at a specified index and return (item removed, resulting list)
def remove(anylist, index):
    if index < 0 or anylist == None:
        raise IndexError
    if index == 0:
        return (anylist.first, anylist.rest)
    index -=1
    temp = remove(anylist.rest, index)
    return (temp[0], Pair(anylist.first, temp[1]))
