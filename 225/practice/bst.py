
#A StrBst is one of:
# - None
# - BstNode(str, StrBst, StrBst)

class BstNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    def __repr__(self):
        return 'BstNode({}, {}, {})'.format(self.value, self.left, self.right)
    def __eq__(self, other):
        return (type(other) == BstNode and self.value == other.value and self.left == other.left and self.right == other.right)


#search function

#StrBst str --> bool
#does the string occur in the tree?
def search(t, sought):
    if t == None:
        return False
    else:
        if (sought < t.value):
            return search(t.left, sought)
        elif sought > t.value:
            return search(t.right, sought)
        else:
            return True


#insert function

#strbst str --> strbst
#insert the new kew into the bst
def insert(t, key):
    if t == None:
        return BstNode(key, None, None)
    else:
        if key < t.value:
            return BstNode(t.value, insert(t.left, key), t.right)
        return BstNode(t.value, t.left, insert(t.right, key))


#delete function

def find_min(bst):
    current_bst = bst
    while current_bst.left != None:
        current_bst = current_bst.left
    return current_bst.value


#bst value --> bst
#deletes the value in the bst
def delete(bst, value):
    if value < bst.value:
        return (value, BstNode(bst.value, delete(bst.left, value), bst.right))
    elif value > bst.value:
        return (value, BstNode(bst.value, bst.left, delete(bst.right, value)))
    else:
        bst.value = value

    return (value, bst)
