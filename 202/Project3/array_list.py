# a List contains an array, size, capacity
class List:
    def __init__(self, array, size=0, capacity=10):
        self.array = array
        self.size = size
        self.capacity = capacity
    def __eq__(self, other):
        return type(other) == List and self.array == other.array and self.size == other.size and self.capacity == other.capacity
    def __repr__(self):
        return "List(%r, %r, %r)" % (self.array, self.size, self.capacity)

# -> None
# to return an empty list
def empty_list():
    return List([None, None, None, None, None, None, None, None, None, None], 0, 10)

# List, int, int -> List
# to replace a value in a list at a specific index with another value
def add(list, index, value):
    if index < 0 or index > list.capacity:
        raise IndexError
    if list.size == list.capacity:
        list.array += ([None])
        list.capacity += 1
    section = list.size - index
    i = 0
    while i < section:
        end = list.size - i
        list.array[end] = list.array[end - 1]
        i += 1
    list.array[index] = value
    list.size += 1
    return list


# List -> int
# to return the length of a list
def length(array):
    count = 0
    for each in array:
        count += 1
    return count


# List, int -> int
# to return the value and a certain index in a list
def get(list, index):
    if index < 0 or index >= list.size:
        raise IndexError
    return list.array[index]

# List, int, int -> list
# to replace the value at a certain index in a list with a new value
def set(list, index, value):
    if index < 0 or index >= length(list):
        raise IndexError
    list[index] = value
    return list

# List, int -> Tuple
# to remove a value at a certain index and return a new list
def remove(list1, index):
    if index < 0 or index >= list1.size:
        raise IndexError
    remove_value = list1.array[index]
    for t in range(index + 1, list1.capacity):
        list1.array[t-1] = list1.array[t]
    list1.array[-1] = None
    list1.size = list1.size - 1
    return (remove_value, list1)
