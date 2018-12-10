import unittest
from linked_stack import *

class TestStack(unittest.TestCase):
    def test00_interface(self):
        test_stack = empty_stack()
        test_stack = push(test_stack, "foo")
        peek(test_stack)
        _, test_stack = pop(test_stack)
        size(test_stack)
        is_empty(test_stack)



if __name__ == "__main__":
    unittest.main()





'''
import unittest
from linked_stack import *

class TestStack(unittest.TestCase):
    def test00_interface(self):
        test_stack = empty_stack()
        test_stack = push(test_stack, "foo")
        peek(test_stack)
        _, test_stack = pop(test_stack)
        size(test_stack)
        is_empty(test_stack)

    def test_repr(self):
        self.assertEqual(repr(Node(1, None)), 'Node(1, None)')
    def test_eq(self):
        self.assertEqual(Node(2, None), Node(2, None)) == Node(2, None), (Node(2, None))


# ---- empty stack ----
    def test_empty(self):
        self.assertEqual(empty_stack(), None)
  
# ---- push ----
    def test_push(self):
        self.assertEqual(push(None, 5), Stack(5, None))
    def test_push2(self):
        self.assertEqual(push(Stack(1, Stack(2, None)), 0), Stack(0, Stack(1, Stack(2, None))))

# ---- pop ----
    def test_pop(self):
        self.assertEqual(pop(None), None)
    def test_pop1(self):
        self.assertEqual(pop(Stack(1, Stack(5, None))), (1, Stack(5, None)))

# ---- peek ----
    def test_peek(self):
        self.assertEqual(peek(None), None)
    def test_peek2(self):
        self.assertEqual(peek(Stack(34, Stack(2, None))), 34)

# ---- size ----
    def test_size(self):
        self.assertEqual(size(None), 0)
    def test_size2(self):
        self.assertEqual(size(Stack(5, Stack(8, None))), 2)

# ---- is empty ----
    def test_is_empty(self):
        self.assertEqual(is_empty(None), True)
    def test_is_empty2(self):
        self.assertEqual(is_empty(Stack(4, None)), False)


if __name__ == "__main__":
    unittest.main()
'''
