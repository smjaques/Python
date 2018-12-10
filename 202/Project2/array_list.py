from operator import *


class List:
    def __init__(self, list, size, capacity):
        self.list = list
        self.size = size
        self.capacity = capacity
    def __eq__(self, other):
        return (type(other) == List and self.list == other.list and self.size == other.size and self.capacity == other.capacity)
    def __repr__(self):
        return 'List({}, {}, {})'.format(self.list, self.size, self.capacity)

#list func --> None
#so you are able to run a function within a loop and keep track of where you are in the list
def foreach(list, order, func):
    rang = length(list)
    i = 0
    while i < rang:
        func(list.list[i], order)
        order += 1
        i += 1



def sort(alist, func):
    for song in range(length(alist)-1, 0, -1):
        maxposition = 0
        for loc in range(1, song+1):
            if func(get(alist, maxposition), get(alist, loc)):
                maxposition = loc
        temp = get(alist, song)
        posmax  = get(alist, maxposition)
        set(alist, song, posmax)
        set(alist, maxposition, temp)
    return alist


#  --> empty list
#function takes no arguments and returns an empty list
def empty_list():
    return List([], 0, 0)


#alist index value --> alist
#returns a new list with the value placed at the given index
def add(alist, index, value):
    if index < 0 or index > alist.capacity:
        raise IndexError
    if alist.size == alist.capacity:
        alist.list += ([None] * 1)
        alist.capacity += 1
    rang = alist.size - index
    i = 0
    while i < rang:
        end = alist.size - i
        alist.list[end] = alist.list[end-1]
        i += 1
    alist.list[index] = value
    alist.size += 1
    return alist
'''


#ADD FUNCTION THAT DOUBLES IN SIZE
#add2
def add(alist, index, value):
    if index < 0 or index > alist.capacity:
        raise IndexError
    if index + 1 >= alist.capacity:
        if alist.capacity == 0:
            alist.capacity = 1
        expand(alist)
    else:
        for x in range(index, alist.capacity-1):
            alist.list[alist.capacity-x-1] = alist.list[alist.capacity-x-2]
    alist.list[index] = value
    alist.size += 1
    return alist
def expand(alist):
    newarr = [None] * (alist.capacity * 2)
    alist.capacity *=2
    for x in range(0, alist.size):
        newarr[x] = alist.list[x]
    alist.list = newarr

'''
#alist --> int
#returns the length of the list
def length(alist):
    return alist.size


#alist index --> int
#returns the value at the index position in the list
def get(alist, index):
    if index >= alist.size:
    #if index < 0 or index >= alist.size:
        raise IndexError
    else:
        return alist.list[index]


#list index value --> list
#function replaces the element at index position in the list with the given value
def set(alist, index, value):
    if index < 0 or index > alist.size:
        raise IndexError
    else:
       alist.list[index] = value
       return alist


#list index --> tuple
#removes the value at the given index and returns (removed item, resulting list)
def remove(alist, index):
    if index < 0 or index > alist.size:
        raise IndexError
    new_size = alist.size -1
    remove = alist.list[index]
    for i in range(index+1, alist.capacity):
        alist.list[i-1]=alist.list[i]

    alist.list[-1] = None
    alist.size = new_size

    return (remove, alist)
