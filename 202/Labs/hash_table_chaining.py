# using the built in python list implementation
# a HashTable is a list of lists with a size
class HashTable:
    def __init__(self, list, size, capacity, collisions=0):
        self.list = list              # a list of lists
        self.size = size              # a number representing the size of the HashTable
        self.capacity = capacity      # a number representing how many indexes exist in the main list
        self.collisions = collisions  # a number that represents the number of collisions
    def __eq__(self, other):
        return type(other) == HashTable and self.list == other.list and self.size == other.size and self.capacity == other.capacity and self.collisions == other.collisions
    def __repr__(self):
        return "HashTable(%r, %r, %r, %r)" % (self.list, self.size, self.capacity, self.collisions)

# -> empty Hash Table
# to create an empty Hash Table with an initial size of 8
def empty_hash_table():
    hash_list = [[None], [None], [None], [None], [None], [None], [None], [None]]

    hash_table = HashTable(hash_list, 0, 8, 0)
    return hash_table


# Hast Table, key, item -> Hash Table
# to add an item into the Hash Table and rehash everything if the table is too big
def insert(table, key, item):
    item_tuple = (item, key)
    index = hash(key)%table.capacity
    sub_list = table.list[index]

    # the sub list has more than one tuple so we have to go through and check all the keys
    if len(sub_list) > 1:
        i = 0
        condition = True
        for object in sub_list:
            if object[1] == item_tuple[1]:
                sub_list[i] = item_tuple
                table.collisions += 1
                condition = False
            i += 1
        if condition == True:
            sub_list.append(item_tuple)
            table.size += 1
            table.collisions += 1

    # the sub list only has one tuple so we have to check the key
    # either have to replace the value that is None, or has the same key
    # otherwise just add the new item to the end of the sub list
    else:
        if sub_list[0] is None:
            sub_list[0] = item_tuple
            table.size += 1
        elif sub_list[0][1] == item_tuple[1]:
            sub_list[0] = item_tuple
            table.collisions += 1
        else:
            sub_list.append(item_tuple)
            table.size += 1
            table.collisions += 1

    if load_factor(table) > 1.5:
        temp_table_list = table.list
        table.capacity *= 2
        table.list = []
        table.collisions = 0
        j = 0
        while j < table.capacity:
            table.list.append([None])
            j += 1
        table.size = 0

        # rehash
        for sub_list in temp_table_list:
            if sub_list != [None]:
                for tuple in sub_list:
                    item = tuple[0]
                    key = tuple[1]
                    insert(table, key, item)

    return table

# Hash Table, key -> int
# to lookup an item at a given spot in a hash table
def get(table, key):
    index = hash(key)%table.capacity
    if table.list[index][0] is None:
        raise LookupError
    else:
        sub_list = table.list[index]
        for tuple in sub_list:
            if tuple[1] == key:
                return tuple[0]

# Hash Table, key -> Hash Table
# to remove an item from a Hash Table and return the resulting HashTable
def remove(table, key):
    index = hash(key)%table.capacity
    if table.list[index][0] is None:
        raise LookupError
    else:
        sub_list = table.list[index]
        i = 0
        for tuple in sub_list:
            if tuple[1] == key:
                sub_list.pop(i)

                table.size -= 1
            i += 1
    return table

# Hash Table -> int
# to determine the number of items in a Hash Table
def size(table):
    return table.size

# Hash Table -> int
# to determine the load factor of a Hash Table
def load_factor(table):
    return table.size/table.capacity

# Hash Table -> int
# to determine the number of collisions in a Hash Table
def collisions(table):
    return table.collisions

