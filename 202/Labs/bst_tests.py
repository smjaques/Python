import unittest
from bst import *


def comes_before(zero, one):
    if zero < one:
        return True
    else:
        return False


class TestList(unittest.TestCase):
    def test_repr_bst(self):
        bst = BinarySearchTree(comes_before, TreeNode(1, None, None))
        self.assertEqual(bst.__repr__(), "BinarySearchTree('comes_before', TreeNode(1, None, None))")

    def test_comes_before_true(self):
        self.assertEqual(comes_before(0, 1), True)

    def test_comes_before_false(self):
        self.assertEqual(comes_before(1, 0), False)

    def test_is_empty_true(self):
        bst1 = BinarySearchTree(comes_before, None)
        self.assertEqual(is_empty(bst1), True)

    def test_is_empty_false(self):
        bst2 = BinarySearchTree(comes_before, TreeNode(1, None, None))
        self.assertEqual(is_empty(bst2), False)

    def test_insert_node_mt(self):
        node1 = None
        node2 = TreeNode(1, None, None)
        self.assertEqual(insert_node(node1, comes_before, 1), node2)

    def test_insert_node_one_left(self):
        node1 = TreeNode(2, None, None)
        node2 = TreeNode(2, TreeNode(1, None, None), None)
        self.assertEqual(insert_node(node1, comes_before, 1), node2)

    def test_insert_node_one_right(self):
        node1 = TreeNode(2, None, None)
        node2 = TreeNode(2, None, TreeNode(3, None, None))
        self.assertEqual(insert_node(node1, comes_before, 3), node2)

    def test_insert_mt(self):
        bst1 = BinarySearchTree(comes_before, None)
        bst2 = BinarySearchTree(comes_before, TreeNode(2, None, None))
        self.assertEqual(insert(bst1, 2), bst2)

    def test_insert_one_left(self):
        bst1 = BinarySearchTree(comes_before, TreeNode(2, None, None))
        bst2 = BinarySearchTree(comes_before, TreeNode(2, TreeNode(1, None, None), None))
        self.assertEqual(insert(bst1, 1), bst2)

    def test_insert_one_right(self):
        bst1 = BinarySearchTree(comes_before, TreeNode(2, None, None))
        bst2 = BinarySearchTree(comes_before, TreeNode(2, None, TreeNode(3, None, None)))
        self.assertEqual(insert(bst1, 3), bst2)

    def test_lookup_node_mt(self):
        node1 = None
        self.assertEqual(lookup_node(node1, comes_before, 1), False)

    def test_lookup_node_one_true(self):
        node1 = TreeNode(1, None, None)
        self.assertEqual(lookup_node(node1, comes_before, 1), True)

    def test_lookup_node_one_false(self):
        node1 = TreeNode(1, None, None)
        self.assertEqual(lookup_node(node1, comes_before, 2), False)

    def test_lookup_node_two_left(self):
        node1 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
        self.assertEqual(lookup_node(node1, comes_before, 1), True)

    def test_lookup_node_two_right(self):
        node1 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
        self.assertEqual(lookup_node(node1, comes_before, 3), True)

    def test_lookup_node_two_false(self):
        node1 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
        self.assertEqual(lookup_node(node1, comes_before, 4), False)

    def test_lookup_mt(self):
        bst1 = BinarySearchTree(comes_before, None)
        self.assertEqual(lookup(bst1, 1), False)

    def test_lookup_one_true(self):
        bst1 = BinarySearchTree(comes_before, TreeNode(1, None, None))
        self.assertEqual(lookup(bst1, 1), True)

    def test_lookup_one_false(self):
        bst1 = BinarySearchTree(comes_before, TreeNode(1, None, None))
        self.assertEqual(lookup(bst1, 2), False)

    def test_lookup_two_left(self):
        node1 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
        bst1 = BinarySearchTree(comes_before, node1)
        self.assertEqual(lookup(bst1, 1), True)

    def test_lookup_two_right(self):
        node1 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
        bst1 = BinarySearchTree(comes_before, node1)
        self.assertEqual(lookup(bst1, 3), True)

    def test_lookup_two_false(self):
        node1 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
        bst1 = BinarySearchTree(comes_before, node1)
        self.assertEqual(lookup(bst1, 4), False)

    def test_delete_node_mt(self):
        node1 = None
        node2 = None
        self.assertEqual(delete_node(node1, comes_before, 1), node2)

    def test_delete_node_one_existent(self):
        node1 = TreeNode(1, None, None)
        node2 = None
        self.assertEqual(delete_node(node1, comes_before, 1), node2)

    def test_delete_node_one_nonexistent(self):
        node1 = TreeNode(1, None, None)
        node2 = TreeNode(1, None, None)
        self.assertEqual(delete_node(node1, comes_before, 2), node2)

    def test_delete_node_two_root(self):
        node1 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
        node2 = TreeNode(3, TreeNode(1, None, None), None)
        self.assertEqual(delete_node(node1, comes_before, 2), node2)

    def test_delete_node_two_no_left(self):
        node1 = TreeNode(2, None, TreeNode(3, None, None))
        node2 = TreeNode(3, None, None)
        self.assertEqual(delete_node(node1, comes_before, 2), node2)

    def test_delete_node_two_no_right(self):
        node1 = TreeNode(2, TreeNode(1, None, None), None)
        node2 = TreeNode(1, None, None)
        self.assertEqual(delete_node(node1, comes_before, 2), node2)

    def test_delete_node_two_right(self):
        node1 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
        node2 = TreeNode(2, TreeNode(1, None, None), None)
        self.assertEqual(delete_node(node1, comes_before, 3), node2)

    def test_delete_node_two_left(self):
        node1 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
        node2 = TreeNode(2, None, TreeNode(3, None, None))
        self.assertEqual(delete_node(node1, comes_before, 1), node2)

    def test_delete_node_three_root(self):
        node1 = TreeNode(3, TreeNode(1, TreeNode(0, None, None), TreeNode(2, None, None)),
                         TreeNode(5, TreeNode(4, None, None), TreeNode(6, None, None)))
        node2 = TreeNode(4, TreeNode(1, TreeNode(0, None, None), TreeNode(2, None, None)),
                         TreeNode(5, None, TreeNode(6, None, None)))
        self.assertEqual(delete_node(node1, comes_before, 3), node2)

    def test_delete_node_three_left(self):
        node1 = TreeNode(3, TreeNode(1, TreeNode(0, None, None), TreeNode(2, None, None)),
                         TreeNode(5, TreeNode(4, None, None), TreeNode(6, None, None)))
        node2 = TreeNode(3, TreeNode(2, TreeNode(0, None, None), None),
                         TreeNode(5, TreeNode(4, None, None), TreeNode(6, None, None)))
        self.assertEqual(delete_node(node1, comes_before, 1), node2)

    def test_delete_node_three_right(self):
        node1 = TreeNode(3, TreeNode(1, TreeNode(0, None, None), TreeNode(2, None, None)),
                         TreeNode(5, TreeNode(4, None, None), TreeNode(6, None, None)))
        node2 = TreeNode(3, TreeNode(1, TreeNode(0, None, None), TreeNode(2, None, None)),
                         TreeNode(6, TreeNode(4, None, None), None))
        self.assertEqual(delete_node(node1, comes_before, 5), node2)

    def test_delete_node_big(self):
        node1 = TreeNode(10, TreeNode(3, None, None),
                         TreeNode(14, TreeNode(13, None, None),
                                  TreeNode(19, TreeNode(15, None,
                                                        TreeNode(17, TreeNode(16, None, None), None)), None)))
        node2 = TreeNode(10, TreeNode(3, None, None),
                         TreeNode(15, TreeNode(13, None, None),
                                  TreeNode(19, TreeNode(17, TreeNode(16, None, None), None), None)))
        self.assertEqual(delete_node(node1, comes_before, 14), node2)

    def test_delete_mt(self):
        bst1 = BinarySearchTree(comes_before, None)
        self.assertEqual(delete(bst1, 1), bst1)

    def test_delete_one(self):
        bst1 = BinarySearchTree(comes_before, TreeNode(1, None, None))
        bst2 = BinarySearchTree(comes_before, None)
        self.assertEqual(delete(bst1, 1), bst2)


if __name__ == '__main__':
    unittest.main()

