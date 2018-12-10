from linked_list import *

class Queue:
    def __init__(self, front, back):
        self.front = front # an Anylist
        self.back = back # an Anylist

    def __eq__(self, other):
        return (type(other) == Queue
                and self.front == other.front
                and self.back == other.back
                )

    def __repr__(self):
        return "Queue(%r, %r)" % (self.front, self.back)

# None -> Queue
# returns an empty Queue
def empty_queue():
    return Queue(None, None)

# Queue value -> Queue
# adds the value to the back of the Queue
def enqueue(q, value):
    if q.front == None:
        q.front = add(q.front, 0, value)
    else:
        q.back = add(q.back, 0, value)
    return q

# Queue -> (value, Queue)
# removes the front of the queue, raising an IndexError if there is no such element
def dequeue(q):
    if q.front is None:
        if q.back is None:
            raise IndexError
        new_front = reverse(q.back)
        value = remove(new_front, 0)[0]

        return (value, Queue(new_front.rest, None))
    value = remove(q.front, 0)[0]
    return (value, Queue(q.front.rest, q.back))

# Queue -> value
# returns the element at the beginning of the queue, raising an IndexError if there is no
# such element
def peek(q):
    if q.front is None: #check back, reverse back
        raise IndexError
    else:
        return q.front.first

# Queue -> int
# returns the number of elements in the given Queue
def size(q):
    return length(q.front) + length(q.back)

# Queue -> boolean
# determines whether or not the given Queue is empty
def is_empty(q):
    return length(q.front) == 0 and length(q.back) == 0



#code: 5c9pw3
