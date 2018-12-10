import unittest
from priority_queue import *

class TestCases(unittest.TestCase):

    def test_empty_pqueue(self):
        self.assertEqual(empty_pqueue(5), Pqueue(None, 5))

    def test_comes_before(self):
        self.assertTrue(comes_before(1, 23))
        self.assertFalse(comes_before(3, 1))

    def test_enqueue(self):
        pqueue = Pqueue(Pair(1, Pair(3, Pair(4, None))), comes_before)
        value = 2
        pqueue2 = Pqueue(Pair(1, Pair(2, Pair(3, Pair(4, None)))), comes_before)
        self.assertEqual(enqueue(pqueue, value), pqueue2)
        pqueue3 = Pqueue(Pair(0, Pair(1, Pair(2, Pair(3, Pair(4, None))))), comes_before)
        self.assertEqual(enqueue(pqueue2, 0), pqueue3)

    def test_remove_1(self):
        anylist = Pair(2, Pair(3, Pair(4, Pair(5, None))))
        index = 1
        self.assertEqual(remove(anylist, index), (3, Pair(2, Pair(4, Pair(5, None)))))

    def test_remove_2(self):
        anylist = Pair(4, None)
        index = 0
        self.assertEqual(remove(anylist, index), (4, None))

    def test_remove_3(self):
        anylist = Pair(3, None)
        index1 = 1
        index2 = -1
        self.assertRaises(IndexError, remove, anylist, index1)
        self.assertRaises(IndexError, remove, anylist, index2)

    def test_remove_4(self):
        anylist = Pair(4, Pair(5, Pair(6, None)))
        index = 2
        self.assertEqual(remove(anylist, index), (6, Pair(4, Pair(5, None))))

    def test_dequeue_1(self):
        pqueue = Pqueue(Pair(1, Pair(3, Pair(4, None))), comes_before)
        pqueue2 = Pqueue(Pair(3, Pair(4, None)), comes_before)
        pqueue3 = empty_pqueue(comes_before)
        pqueue4 = Pqueue(Pair(4, None), comes_before)
        pqueue5 = Pqueue(None, comes_before)
        self.assertEqual(dequeue(pqueue), (1, pqueue2))
        self.assertRaises(IndexError, dequeue, pqueue3)
        self.assertEqual(dequeue(pqueue4), (4, pqueue5))

    def test_get_1(self):
        anylist = Pair(4, Pair(5, None))
        index = 0
        self.assertEqual(get(anylist, index), 4)

    def test_get_2(self):
        anylist = Pair(3, Pair(5, Pair(6, None)))
        index = 2
        self.assertEqual(get(anylist, index), 6)

    def test_get_3(self):
        anylist = Pair(3, Pair(5, Pair(6, None)))
        index1 = 3
        index2 = -1
        self.assertRaises(IndexError, get, anylist, index1)
        self.assertRaises(IndexError, get, anylist, index2)

    def test_peek_1(self):
        pqueue = Pqueue(Pair(1, Pair(3, Pair(4, None))), comes_before)
        pqueue2 = Pqueue(None, comes_before)
        self.assertEqual(peek(pqueue), 1)
        self.assertRaises(IndexError, peek, pqueue2)

    def test_length_1(self):
        anylist = Pair(5, Pair(6, Pair(3, None)))
        self.assertEqual(length(anylist), 3)

    def test_length_2(self):
        self.assertEqual(length(None), 0)

    def test_length_3(self):
        anylist = Pair(4, None)
        self.assertEqual(length(anylist), 1)

    def test_size_1(self):
        pqueue = Pqueue(Pair(1, Pair(3, Pair(4, None))), comes_before)
        pqueue2 = Pqueue(None, comes_before)
        self.assertEqual(size(pqueue), 3)
        self.assertEqual(size(pqueue2), 0)

    def test_is_empty(self):
        pqueue = Pqueue(None, comes_before)
        pqueue2 = Pqueue(Pair(1, None), comes_before)
        self.assertTrue(is_empty(pqueue))
        self.assertFalse(is_empty(pqueue2))

    def test_eq(self):
        pqueue = Pqueue(None, comes_before)
        pqueue2 = Pqueue(None, comes_before)
        self.assertEqual(pqueue, pqueue2)

    def test_repr(self):
        pqueue = Pqueue(None, 5)
        self.assertEqual(repr(pqueue), "Pqueue(None, 5)")

    def test_Pair(self):
        pair1 = Pair(1, None)
        pair2 = Pair(1, None)
        pair3 = Pair(2, None)
        self.assertEqual(pair1, pair2)
        self.assertNotEqual(pair1, pair3)
        self.assertEqual(repr(pair1), 'Pair(1, None)')
        self.assertEqual(pair1.first, 1)
        self.assertEqual(pair1.rest, None)

    def test_insert_empty(self):
        list1 = None
        self.assertEqual(insert(1, comes_before, list1), Pair(1, None))



if __name__ == "__main__":
    unittest.main()


