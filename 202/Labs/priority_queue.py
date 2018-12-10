import sys
sys.setrecursionlimit(10000)


# a Linked List is one of the following
# - None
# Pair

class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest
    def __repr__(self):
        return "Pair(%r, %r)" % (self.first, self.rest)
    def __eq__(self, other):
        return type(other) == Pair and self.first == other.first and self.rest == other.rest

class Pqueue:
    def __init__(self, queue, comes_before):
        self.queue = queue                   # a Linked List
        self.comes_before = comes_before     # an ordering function
    def __eq__(self, other):
        return type(other) == Pqueue and self.queue == other.queue and self.comes_before == other.comes_before
    def __repr__(self):
        return "Pqueue(%r, %r)" % (self.queue, self.comes_before)



# func -> Pqueue
# to return an empty Pqueue
def empty_pqueue(func):
    return Pqueue(None, func)


# int, int -> int
# to determine the smaller value, this function was made to help with testing
def comes_before(a, b):
    return a < b


# value, func, linked list -> linked list
# to add a value to an already sorted linked list
def insert(value, func, sorted_list):
    if sorted_list == None:
        return Pair(value, None)
    if not func(value, sorted_list.first):
        return Pair(sorted_list.first, insert(value, func, sorted_list.rest))
    return Pair(value, Pair(sorted_list.first, sorted_list.rest))

# value, Pqueue -> Pqueue
# to add a value in the proper location in a Pqueue
def enqueue(pqueue, value):
    pqueue.queue = insert(value, pqueue.comes_before, pqueue.queue)
    return Pqueue(pqueue.queue, pqueue.comes_before)

'''def enqueue(pq, value):
    if pq.queue is None:
        pq.queue = Pair(value, None)
    else:
        if pq.comes_before(value, pq.queue.first):
            pq.queue = Pair(value, pq.queue)
        else:
            pq.queue = Pair(pq.queue.first, enqueue(Pqueue(pq.queue.rest, pq.comes_before),
                          value).queue)
    return pq'''

# linked list, index -> linked list
# to remove an item in a linked list
def remove(anylist, index):
    if index < 0 or anylist == None:
        raise IndexError
    if index == 0:
        return (anylist.first, anylist.rest)
    index -= 1
    temp = remove(anylist.rest, index)
    return (temp[0], Pair(anylist.first, temp[1]))

# Pqueue -> tuple
# removes the item at the beginning of a Pqueue
def dequeue(pqueue):
    data = remove(pqueue.queue, 0)
    value = data[0]
    new_queue = data[1]
    return (value, Pqueue(new_queue, pqueue.comes_before))

# linked list, int -> value
# to return the value at a specific index in a linked list
def get(anylist, index):
    if index < 0 or anylist == None:
        raise IndexError
    if index == 0:
        return anylist.first
    index -= 1
    return get(anylist.rest, index)

# Pqueue -> value
# returns the value at the beginning of a Pqueue
def peek(pqueue):
    value = get(pqueue.queue, 0)
    return value

# linked list -> int
# to determine the number of elements in a linked list
def length(anylist):
    if anylist == None:
        return 0
    return 1 + length(anylist.rest)

# Pqueue -> int
# to determine the number of elements in a Pqueue
def size(pqueue):
    size = length(pqueue.queue)
    return size

# Pqueue -> Boolean
# to determine if a Pqueue is empty
def is_empty(pqueue):
    return pqueue.queue is None


















