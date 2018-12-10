import unittest
from bst import *


def comes_before(zero, one):
    if zero < one:
        return True
    else:
        return False


class TestList(unittest.TestCase):
    def test_prefix_node_mt(self):
        iter = prefix_node(None)
        self.assertRaises(StopIteration, next, iter)

    def test_prefix_node_one(self):
        iter = prefix_node(TreeNode(1, None, None))
        self.assertEqual(next(iter), 1)
        self.assertRaises(StopIteration, next, iter)

    def test_prefix_node_two_left(self):
        iter = prefix_node(TreeNode(2, TreeNode(1, None, None), None))
        self.assertEqual(next(iter), 2)
        self.assertEqual(next(iter), 1)
        self.assertRaises(StopIteration, next, iter)

    def test_prefix_node_two_right(self):
        iter = prefix_node(TreeNode(2, None, TreeNode(3, None, None)))
        self.assertEqual(next(iter), 2)
        self.assertEqual(next(iter), 3)
        self.assertRaises(StopIteration, next, iter)

    def test_prefix_node_three(self):
        iter = prefix_node(TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)))
        self.assertEqual(next(iter), 2)
        self.assertEqual(next(iter), 1)
        self.assertEqual(next(iter), 3)
        self.assertRaises(StopIteration, next, iter)

    def test_infix_node_mt(self):
        iter = infix_node(None)
        self.assertRaises(StopIteration, next, iter)

    def test_infix_node_one(self):
        iter = infix_node(TreeNode(1, None, None))
        self.assertEqual(next(iter), 1)
        self.assertRaises(StopIteration, next, iter)

    def test_infix_node_two_left(self):
        iter = infix_node(TreeNode(2, TreeNode(1, None, None), None))
        self.assertEqual(next(iter), 1)
        self.assertEqual(next(iter), 2)
        self.assertRaises(StopIteration, next, iter)

    def test_infix_node_two_right(self):
        iter = infix_node(TreeNode(2, None, TreeNode(3, None, None)))
        self.assertEqual(next(iter), 2)
        self.assertEqual(next(iter), 3)
        self.assertRaises(StopIteration, next, iter)

    def test_infix_node_three(self):
        iter = infix_node(TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)))
        self.assertEqual(next(iter), 1)
        self.assertEqual(next(iter), 2)
        self.assertEqual(next(iter), 3)
        self.assertRaises(StopIteration, next, iter)

    def test_infix_node_seven(self):
        node = TreeNode(4, TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)),
                        TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, None)))
        iter = infix_node(node)
        self.assertEqual(next(iter), 1)
        self.assertEqual(next(iter), 2)
        self.assertEqual(next(iter), 3)
        self.assertEqual(next(iter), 4)
        self.assertEqual(next(iter), 5)
        self.assertEqual(next(iter), 6)
        self.assertEqual(next(iter), 7)
        self.assertRaises(StopIteration, next, iter)

    def test_postfix_node_mt(self):
        iter = postfix_node(None)
        self.assertRaises(StopIteration, next, iter)

    def test_postfix_node_one(self):
        iter = postfix_node(TreeNode(1, None, None))
        self.assertEqual(next(iter), 1)
        self.assertRaises(StopIteration, next, iter)

    def test_postfix_node_two_left(self):
        iter = postfix_node(TreeNode(2, TreeNode(1, None, None), None))
        self.assertEqual(next(iter), 1)
        self.assertEqual(next(iter), 2)
        self.assertRaises(StopIteration, next, iter)

    def test_postfix_node_two_right(self):
        iter = postfix_node(TreeNode(2, None, TreeNode(3, None, None)))
        self.assertEqual(next(iter), 3)
        self.assertEqual(next(iter), 2)
        self.assertRaises(StopIteration, next, iter)

    def test_postfix_node_three(self):
        iter = postfix_node(TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)))
        self.assertEqual(next(iter), 1)
        self.assertEqual(next(iter), 3)
        self.assertEqual(next(iter), 2)
        self.assertRaises(StopIteration, next, iter)

    def test_prefix_iterator(self):
        node = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
        bst = BinarySearchTree(comes_before, node)
        iter = prefix_iterator(bst)
        self.assertEqual(next(iter), 2)
        self.assertEqual(next(iter), 1)
        self.assertEqual(next(iter), 3)
        self.assertRaises(StopIteration, next, iter)

    def test_infix_iterator(self):
        node = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
        bst = BinarySearchTree(comes_before, node)
        iter = infix_iterator(bst)
        self.assertEqual(next(iter), 1)
        self.assertEqual(next(iter), 2)
        self.assertEqual(next(iter), 3)
        self.assertRaises(StopIteration, next, iter)

    def test_postfix_iterator(self):
        node = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
        bst = BinarySearchTree(comes_before, node)
        iter = postfix_iterator(bst)
        self.assertEqual(next(iter), 1)
        self.assertEqual(next(iter), 3)
        self.assertEqual(next(iter), 2)
        self.assertRaises(StopIteration, next, iter)


if __name__ == '__main__':
    unittest.main()

