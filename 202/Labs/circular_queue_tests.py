import unittest
from circular_queue import *

class TestQueue(unittest.TestCase):
    def test00_interface(self):
        test_queue = empty_queue()
        test_queue = enqueue(test_queue, "foo")
        peek(test_queue)
        _, test_queue = dequeue(test_queue)
        size(test_queue)
        is_empty(test_queue)

    def test_eq(self):
        queue1 = [None] * 5000
        queue2 = [None] * 5000
        self.assertEqual(queue1, queue2)

    def test_repr(self):
        queue = [None] * 5
        self.assertEqual(repr(queue), "[None, None, None, None, None]")

    def test_empty_queue(self):
        queue = Queue()
        self.assertEqual(queue, empty_queue())

    def test_enqueue(self):
        queue = Queue([None]*5000, 0, 0, 0)
        queue2 = Queue([1] + [None] + ([None] * 4998), 1, 1, 1)
        self.assertEqual(enqueue(queue, 1), queue2)
        queue3 = Queue([1] + [2] + [None] + ([None] * 4997), 2, 2, 2)
        self.assertEqual(enqueue(queue2, 2), queue3)
        queue4 = Queue([None]*5000, 50001, 30303030, 303030)
        self.assertRaises(IndexError, enqueue, queue4, 9)

    '''def test_enqueue_1(self):
        queue = Queue([1]*4999 + [None], 4999, 0, 4999)
        queue2 = Queue([2] + [1] * 4999, 0, 0, 5000)
        self.assertEqual(enqueue(queue, 2), queue2)'''

    def test_peek(self):
        queue = Queue([None] * 5000, 0, 0, 0)
        self.assertRaises(IndexError, peek, queue)
        queue2 = Queue([3] + [1] + [2] + ([None] * 4997), 2, 2, 3)
        self.assertEqual(peek(queue2), 3)

    def test_size(self):
        queue = Queue([3] + [1] + [2] + ([None] * 4997), 2, 2, 3)
        self.assertEqual(size(queue), 3)

    def test_is_empty(self):
        queue = Queue([None] * 5000, 0, 0, 0)
        self.assertTrue(is_empty(queue))

    def test_dequeue(self):
        queue = Queue([None] * 5000, 0, 0, 0)
        self.assertRaises(IndexError, dequeue, queue)
        queue2 = Queue([4] + [1] * 4999, 0, 4999, 5000)
        queue3 = Queue([None] + [1] * 4999, 0, 0, 4999)
        self.assertEqual(dequeue(queue2), (4, queue3))




if __name__ == "__main__":
    unittest.main()

