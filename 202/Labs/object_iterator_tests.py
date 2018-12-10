import unittest
from linked_list import *

lst1 = None
lst2 = Pair(1, None)
lst3 = Pair(4, Pair(3, Pair(2, Pair(1, None))))
obj1 = object_iterator(lst1)
obj2 = object_iterator(lst2)
obj3 = object_iterator(lst3)


class TestList(unittest.TestCase):
    def test_object_iterator(self):
        self.assertEqual(object_iterator(None), obj1)

    def test_has_next_false(self):
        self.assertEqual(has_next(obj1), False)

    def test_has_next_true(self):
        self.assertEqual(has_next(obj2), True)

    def test_next_small(self):
        self.assertEqual(next(obj2), 1)
        self.assertRaises(StopIteration, next, obj2)

    def test_next_big(self):
        self.assertEqual(next(obj3), 4)
        self.assertEqual(next(obj3), 3)
        self.assertEqual(next(obj3), 2)
        self.assertEqual(next(obj3), 1)
        self.assertRaises(StopIteration, next, obj3)

    def test_next_error(self):
        self.assertRaises(StopIteration, next, obj1)
        
    
    def test_repr(self):
        self.assertEqual(repr(self.obj1), "Iterator(None)")
     


if __name__ == '__main__':
    unittest.main()

