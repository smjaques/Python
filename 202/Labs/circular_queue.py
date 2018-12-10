# queue is array list of length 5000
# list- list of 5000 elements
# head - index of last element in array
class Queue:
    def __init__(self, list=[None]*5000, head=0, tail=0, size=0):
        self.list = list
        self.head = head
        self.tail = tail
        self.size = size

    def __eq__(self, other):
        return ((type(other) == Queue) and self.list == other.list and self.head == other.head)

    def __repr__(self):
        return ("%r" % (self.list))
# -> Queue
# return an empty queue
def empty_queue():
    return Queue()


# Queue, integer -> Queue
# return new queue with value added to end
def enqueue(queue, value):
    if queue.size != 5000:
        if queue.head != 4999:
            queue.list[queue.head] = value
            queue.head = queue.head + 1
            queue.size = queue.size + 1
        #else:
           # queue.list[0] = value

            #queue.head = 0
            #queue.size += 1
        return queue
    else:
        raise IndexError()

# Queue -> Queue
# return new queue after removing first element
def dequeue(queue):
    if (queue.list[queue.tail] != None):
        temp = queue.list[0]
        queue.list[0] = None
        if queue.tail == 4999:
            queue.tail = 0
        else:
            queue.tail = queue.tail + 1
        queue.size = queue.size - 1
        return (temp, queue)
    else:
        raise IndexError()

# Queue -> integer
# return element at beginning of queue
def peek(queue):
    if queue.list[0] == None:
        raise IndexError()
    else:
        return queue.list[0]

# Queue -> integer
# return size of queue
def size(queue):
    return queue.size

def is_empty(queue):
    return queue.size == 0
