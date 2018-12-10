import unittest
from linked_list import yield_iterator, Pair


class TestList(unittest.TestCase):
    def test_yield_iterator_short(self):
        iter = yield_iterator(Pair(1, None))
        self.assertEqual(next(iter), 1)
        self.assertRaises(StopIteration, next, iter)

    def test_yield_iterator_big(self):
        iter = yield_iterator(Pair(4, Pair(3, Pair(2, Pair(1, None)))))
        self.assertEqual(next(iter), 4)
        self.assertEqual(next(iter), 3)
        self.assertEqual(next(iter), 2)
        self.assertEqual(next(iter), 1)
        self.assertRaises(StopIteration, next, iter)


if __name__ == '__main__':
    unittest.main()

