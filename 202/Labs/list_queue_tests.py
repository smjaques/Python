import unittest
from list_queue import *

class TestQueue(unittest.TestCase):
    def test00_interface(self):
        test_queue = empty_queue()
        test_queue = enqueue(test_queue, "foo")
        peek(test_queue)
        _, test_queue = dequeue(test_queue)
        size(test_queue)
        is_empty(test_queue)

    def test_eq(self):
        queue1 = Queue(Pair(4, None), Pair(5, None))
        queue2 = Queue(Pair(4, None), Pair(5, None))
        self.assertEqual(queue1, queue2)

    def test_enqueue(self):
        queue = Queue(Pair(5, None), Pair(4, None))
        queue2 = Queue(Pair(5, None), Pair(3, Pair(4, None)))
        self.assertEqual(enqueue(queue, 3), queue2)

    def test_enqueue_2(self):
        queue = Queue(Pair(5, None), None)
        queue2 = Queue(Pair(5, None), Pair(4, None))
        self.assertEqual(enqueue(queue, 4), queue2)

    def test_peek(self):
        queue = Queue(Pair(5, Pair(8, None)), Pair(4, Pair(7, None)))
        self.assertEqual(peek(queue), 5)

    def test_remove(self):
        queue = Queue(Pair(5, Pair(8, None)), Pair(4, Pair(7, None)))
        self.assertEqual(dequeue(queue), (5, Queue(Pair(8, None), Pair(4, Pair(7, None)))))

    def test_dequeue_error(self):
        queue = Queue(None, None)
        self.assertRaises(IndexError, dequeue, queue)

    def test_peek_error(self):
        queue = Queue(None, None)
        self.assertRaises(IndexError, peek, queue)

    def test_dequeue_1(self):
        queue = Queue(Pair(9, Pair(8, Pair(7, None))), Pair(6, Pair(8, Pair(4, None))))
        queue2 = Queue(Pair(8, Pair(7, None)), Pair(6, Pair(8, Pair(4, None))))
        self.assertEqual(dequeue(queue), (9, queue2))

    def test_empty_queue(self):
        self.assertEqual(empty_queue(), Queue(None, None))

    def test_enqueue_empty(self):
        self.assertEqual(peek(enqueue(empty_queue(), 10)), 10)

    '''def test_enqueue_full(self):
        lst1 = Pair(1, Pair(2, Pair(3, None)))
        lst2 = Pair(3, Pair(2, Pair(1, None)))
        q1 = Queue(lst1, lst2)
        lst3 = Pair(1, Pair(2, Pair(3, None)))
        lst4 = Pair(4, None)
        q2 = Queue(lst3, lst4)
        self.assertEqual(enqueue(q1, 4), q2)'''

    def test_dequeue_empty(self):
        self.assertRaises(IndexError, dequeue, empty_queue())

    def test_dequeue_full(self):
        lst1 = Pair(1, Pair(2, Pair(3, None)))
        lst2 = None
        q1 = Queue(lst1, lst2)
        self.assertEqual(dequeue(q1), (1, Queue(Pair(2, Pair(3, None)), None)))

    def test_dequeue_full_reverse(self):
        lst1 = None
        lst2 = Pair(1, Pair(2, Pair(3, None)))
        q1 = Queue(lst1, lst2)
        self.assertEqual(dequeue(q1), (3, Queue(Pair(2, Pair(1, None)), None)))

    def test_peek_empty(self):
        self.assertRaises(IndexError, peek, empty_queue())

    def test_peek_full(self):
        lst1 = Pair(1, Pair(2, None))
        lst2 = Pair(2, Pair(1, None))
        q1 = Queue(lst1, lst2)
        self.assertEqual(peek(q1), 1)

    def test_repr(self):
        queue1 = Queue(None, None)
        self.assertEqual(repr(queue1),"Queue(None, None)")

if __name__ == "__main__":
    unittest.main()


