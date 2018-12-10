# Name: Sydney Jaques
# Lab 3- Array List

class List:
    def __init__(self, list, size=0, capacity=0):
        self.list = list
        self.size = size
        self.capacity = capacity
    def __repr__(self):
        return 'List({}, {}, {})'.format(self.list, self.size, self.capacity)

    def __eq__(self, other):
        return ((type(other) == List) and self.list == other.list and self.size == other.size and self.capacity == other.capacity)


#an alist is an array list which each element of the array represents one element of the list



#  --> empty list
#function takes no arguments and returns an empty list
def empty_list():
    return List([], 0, 0)

#alist index value --> alist
#returns a new list with the value placed at the given index
def add(alist, index, value):
    if index < 0 or index > alist.size:
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


            

#alist --> int
#returns the length of the list
def length(alist):
    return alist.size


#alist index --> int
#returns the value at the index position in the list
def get(alist, index):
    if index < 0 or index >= alist.size:
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



    #just like add but remove it and bring everything forward
    #decrease the size by one
    #need to watch index error, i --> i+1 if i becomes greater than capacity set i = None BREAK


    #break breaks out 
    #continue restarts a loop
