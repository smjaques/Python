from array_list import *
import unittest


def func(x, y):
    return x < y

class TestList(unittest.TestCase):



# ---- class ----
    def test_repr(self):
        self.assertEqual(repr(List([1, 2, 3], 3, 3)), 'List([1, 2, 3], 3, 3)')

    def test_eq(self):
        self.assertEqual(List([1, 2, 3], 3, 3) == List([1, 2, 3], 3, 3), True)
        self.assertEqual(List([1, 2, 3, None], 3, 4) == List([1, 2, 3], 3, 3), False)

# ---- for each ----
    def test_foreach(self):
        self.assertEqual(foreach(List([1, 2, 3], 3, 3), 0, func), None)


# ---- new sort ----
    def test_sort(self):
        self.assertEqual(sort(List([1, 3, 2], 3, 3), func), List([1, 2, 3], 3, 3))
    def test_sort2(self):
        self.assertEqual(sort(List([8, 3, 7], 3, 3), func), List([3, 7, 8], 3, 3))




# ---- empty ----
    def test_empty(self):
        self.assertEqual(empty_list(), List([], 0, 0))



# ---- add ----
    def test_add(self):
        with self.assertRaises(IndexError):
            add(List([1, 2, 3], 3, 3), 5, 7)
    def test_add2(self):
        self.assertEqual(add(List([1, 3, 5, 7], 4, 4), 1, 2), List([1, 2, 3, 5, 7], 5, 5))
    def test_add3(self):
        self.assertEqual(add(List([0, 1, 3, 4, 5, None], 5, 6), 2, 2), List([0, 1, 2, 3, 4, 5], 6, 6))
    def test_add4(self):
        self.assertEqual(add(List([3, 4, 2, 1, None, None], 4, 6), 0, 0), List([0, 3, 4, 2, 1, None], 5, 6))
    def test_add5(self):
        self.assertEqual(add(List([None], 0, 1), 0, 0), List([0], 1, 1))
    def test_add6(self):
        self.assertEqual(add(List([None, 1, 2, None], 3, 4), 0, 0), List([0, None, 1, 2], 4, 4))
    def test_add7(self):
        self.assertEqual(add(List([None, None, None, None, None, None, None, None, None, None, None,None], 0, 12), 1, 4), List([None, 4, None, None, None, None, None, None, None, None, None, None], 1, 12))
# ---- length ----
    def test_length(self):
        self.assertEqual(length(List([1, 2, None], 2, 3)), 2)
    def test_length2(self):
        self.assertEqual(length(List([None], 0, 1)), 0)



# ---- get ----
    def test_get(self):
        with self.assertRaises(IndexError):
            get(List([1, 2, 3], 3, 3), 7)
        with self.assertRaises(IndexError):
            get(List([1, 2], 2, 2), -5)
    def test_get2(self):
        self.assertEqual(get(List([0, 56, 32, 564, None, None], 4, 6), 3), 564)



# ---- set ----
    def test_set(self):
        with self.assertRaises(IndexError):
            set(List([1, 2, 3], 3, 3), 4, 1)
        with self.assertRaises(IndexError):
            set(List([1, None, None], 1, 3), -1, -3)
    def test_set2(self):
        self.assertEqual(set(List([64, 343, 54, 76], 4, 4), 1, 0), List([64, 0, 54, 76], 4, 4))
    def test_set3(self):
        self.assertEqual(set(List([12, 54, None], 2, 3), 0, 567), List([567, 54, None], 2, 3))

# ---- remove ----
    def test_remove(self):
        with self.assertRaises(IndexError):
            remove(List([1, 2], 2, 2),  5)
        with self.assertRaises(IndexError):
            remove(List([None, 1, 2, 3], 3, 4), -45)
    def test_remove2(self):
        self.assertEqual(remove(List([1, 2, 3, 3, 4], 5, 5), 2), (3, List([1, 2, 3, 4, None], 4, 5)))
    def test_remove3(self):
        self.assertEqual(remove(List([0, 3, 2, None], 3, 4), 1), (3, List([0, 2, None, None], 2, 4)))




if __name__ == '__main__':
    unittest.main()
