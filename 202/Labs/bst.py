#  Sydney Jaques
#  Lab 4 - bst

# represents a Binary Search Tree with an input comparator function
class BinarySearchTree:
    def __init__(self, fn, root=None):
        self.fn = fn  # a function
        self.root = root  # a BSTNode

    def __eq__(self, other):
        return (type(other) == BinarySearchTree
                and self.fn == other.fn
                and self.root == other.root
                )

    def __repr__(self):
        return "BinarySearchTree({!r}, {!r})".format(self.fn.__name__, self.root)


# a BSTNode is one of
# - None, or
# - TreeNode(value, left, right) with values in a sorted order throughout the tree
class TreeNode:
    def __init__(self, value, left, right):
        self.value = value  # any value
        self.left = left  # a BSTNode
        self.right = right  # a BSTNode

    def __eq__(self, other):
        return (type(other) == TreeNode
                and self.value == other.value
                and self.left == other.left
                and self.right == other.right
                )

    def __repr__(self):
        return "TreeNode({!r}, {!r}, {!r})".format(self.value, self.left, self.right)


# BinarySearchTree -> bool
# returns True if the tree is empty, returns False if it is not
def is_empty(bst):
    if bst.root == None:
        return True
    else:
        return False


# TreeNode value fn -> TreeNode
# helper for insert, inserts the value into the tree and returns the node
def insert_node(node, fn, val):
    if node == None:
        return TreeNode(val, None, None)
    else:
        if fn(val, node.value):
            return TreeNode(node.value, insert_node(node.left, fn, val), node.right)
        else:
            return TreeNode(node.value, node.left, insert_node(node.right, fn, val))


# BinarySearchTree value -> BinarySearchTree
# inserts the value into the tree while maintaining BST order, returns the resulting BST
def insert(bst, val):
    bst.root = insert_node(bst.root, bst.fn, val)
    return bst


# TreeNode value fn -> bool
# helper for lookup, checks if the value is in the tree
def lookup_node(node, fn, val):
    if node is None:
        return False
    else:
        if fn(val, node.value):
            return lookup_node(node.left, fn, val)
        elif fn(node.value, val):
            return lookup_node(node.right, fn, val)
        else:
            return True


# BinarySearchTree value -> bool
# checks if the specified value is in the tree
def lookup(bst, val):
    return lookup_node(bst.root, bst.fn, val)


# TreeNode value fn -> TreeNode
# helper for delete, removes the value from the tree and returns the node
def delete_node(node, fn, val):
    if node is None:
        return None
    else:
        if fn(val, node.value):
            return TreeNode(node.value, delete_node(node.left, fn, val), node.right)
        elif fn(node.value, val):
            return TreeNode(node.value, node.left, delete_node(node.right, fn, val))
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                replace = get_minimum_right(node.right)
                node.right = delete_node(node.right, fn, replace)
                node.value = replace
                return node


# TreeNode value fn -> value
# helper for delete_node, returns the leftmost value on the node
def get_minimum_right(node):
    if node.left is None:
        return node.value
    else:
        return get_minimum_right(node.left)


# BinarySearchTree value -> BinarySearchTree
# deletes the value from the tree while maintaining BST order, returns the resulting BSTs
def delete(bst, val):
    bst.root = delete_node(bst.root, bst.fn, val)
    return bst


# TreeNode -> generator
# helper for prefix_iterator, creates a generator for the tree preorder
def prefix_node(node):
    if node is not None:
        yield node.value
        yield from prefix_node(node.left)
        yield from prefix_node(node.right)


# TreeNode -> generator
# helper for infix_iterator, creates a generator for the tree inorder
def infix_node(node):
    if node is not None:
        yield from infix_node(node.left)
        yield node.value
        yield from infix_node(node.right)


# TreeNode -> generator
# helper for postfix_iterator, creates a generator for the tree postorder
def postfix_node(node):
    if node is not None:
        yield from postfix_node(node.left)
        yield from postfix_node(node.right)
        yield node.value


# BinarySearchTree -> generator
# creates a generator for the tree preorder
def prefix_iterator(bst):
    return prefix_node(bst.root)


# BinarySearchTree -> generator
# creates a generator for the tree inorder
def infix_iterator(bst):
    return infix_node(bst.root)


# BinarySearchTree -> generator
# creates a generator for the tree postorder
def postfix_iterator(bst):
    return postfix_node(bst.root)



#code: c0w9b2
