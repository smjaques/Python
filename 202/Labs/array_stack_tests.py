import unittest
from array_stack import *

class TestStack(unittest.TestCase):
    def test00_interface(self):
        test_stack = empty_stack()
        test_stack = push(test_stack, "foo")
        peek(test_stack)
        _, test_stack = pop(test_stack)
        size(test_stack)
        is_empty(test_stack)


    def test_empty_stack(self):
        self.assertEqual(empty_stack(), empty_list())

    def test_push_1(self):
        stack = List([1, 2, 3, 4, 5, None, None, None, None, None], 5, 10)
        stack2 = List([9, 1, 2, 3, 4, 5, None, None, None, None], 6, 10)
        self.assertEqual(push(stack, 9), stack2)

    def test_push_2(self):
        stack = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 10)
        stack2 = List([11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, 11)
        self.assertEqual(push(stack, 11), stack2)

    def test_pop_1(self):
        stack = List([1, 2, 3, 4, 5, None, None, None, None, None], 5, 10)
        stack2 = List([2, 3, 4, 5, None, None, None, None, None, None], 4, 10)
        self.assertEqual(pop(stack), (1, stack2))

    def test_pop_2(self):
        stack = List([1, None, None, None, None, None, None, None, None, None], 1, 10)
        stack2 = List([None, None, None, None, None, None, None, None, None, None], 0, 10)
        self.assertEqual(pop(stack), (1, stack2))

    def test_pop_3(self):
        stack = List([None, None, None, None, None, None, None, None, None, None], 0, 10)
        self.assertRaises(IndexError, pop, stack)

    def test_peek_1(self):
        stack = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 10)
        self.assertEqual(peek(stack), 1)
        stack2 = empty_stack()
        self.assertRaises(IndexError, peek, stack2)

    def test_size_1(self):
        stack = List([1, None, None, None, None, None, None, None, None, None], 1, 10)
        self.assertEqual(size(stack), 1)
        stack2 = List([None, None, None, None, None, None, None, None, None, None], 0, 10)
        self.assertEqual(size(stack2), 0)
        stack3 = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 10)
        self.assertEqual(size(stack3), 10)

    def test_is_empty(self):
        stack = empty_list()
        stack2 = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 10)
        self.assertTrue(is_empty(stack))
        self.assertFalse(is_empty(stack2))





'''
# ---- empty stack ----
    def test_empty(self):
        self.assertEqual(empty_stack(), [])

# ---- push ----
    def test_push(self):
        self.assertEqual(push([], 1), [1])
    def test_push2(self):
        self.assertEqual(push([5, 6, 7], 8), [5, 6, 7, 8])

# ---- pop ----
    def test_pop(self):
        with self.assertRaises(IndexError):
            pop([])
    def test_pop2(self):
        self.assertEqual(pop([1, 2, 3]), (3, [1, 2]))
    def test_pop3(self):
        self.assertEqual(pop([2, 3, 43, 2]), (2, [2, 3, 43]))

# ---- peek ----
    def test_peek(self):
        self.assertEqual(peek([]), None)
    def test_peek2(self):
        self.assertEqual(peek([1, 2, 3]), 3)

# ---- size ----
    def test_size(self):
        self.assertEqual(size([]), 0)
    def test_size2(self):
        self.assertEqual(size([1, 2, 3]), 3)

# ---- is empty ----
    def test_is_empty(self):
        self.assertEqual(is_empty([]), True)
    def test_is_empty2(self):
        self.assertEqual(is_empty([1, 2, 3]), False)

'''




if __name__ == "__main__":
    unittest.main()
