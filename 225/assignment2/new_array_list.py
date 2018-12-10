#Arraylist is one of 
# - None
# - List(list, size, capacity)
class List:
    def __init__(self, list, size=0, capacity=10):
        self.list = list
        self.size = size
        self.capacity = capactiy
    def __eq__(self, other):
        return ((type(other) == List) and self.list == other.list and self.size == other.size and self.capacity == other.capacity
    def __repr__(self):
        return 'List({}, {}, {})'.format(self.list, self.size, self.capacity)
