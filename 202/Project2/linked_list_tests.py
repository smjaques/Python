from linked_list import *
import unittest




# ------ TestCases ------
class TestList(unittest.TestCase):
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")



def func(x, y):
    return x > y


class TestCase(unittest.TestCase):


# ---- class ----
    def test_reprrr(self):
        self.assertEqual(repr(Pair('song', None)), 'Pair(song, None)')
    def test_equal(self):
        self.assertEqual(Pair('0--title--artist--album', None) == Pair('0--title--artist--album', None), True)
        self.assertEqual(Pair('hey', None) == Pair('Hey', None), False)



# ---- length ----
    def test_lengtah(self):
        self.assertEqual(length(None), 0)
    def test_lengtha2(self):
        self.assertEqual(length(Pair('string of songs', Pair('more songs', None))), 2)
    


# ---- insertion sort ----
    def test_sort(self):
        self.assertEqual(insertion_sort(func, 5, None), Pair(5, None))
    def test_sort2(self):
        self.assertEqual(insertion_sort(func, 5, Pair(4, None)), Pair(5, Pair(4, None)))
    def test_sort34(self):
        sorted_list = Pair(5, None)
        self.assertEqual(insertion_sort(func, 3, sorted_list), Pair(5, Pair(3, None)))


# ---- sort ----
    def test_newsort(self):
        self.assertEqual(sort(Pair(4, Pair(1, None)), func), Pair(4, Pair(1, None)))

# --- for each ----
    def test_foreachh(self):
        self.assertEqual(foreach(None, 5, func), None)
    def test_foreach2(self):
        self.assertEqual(foreach(Pair(7, Pair(4, None)), 1, func), None)





# -------- LAB TESTS --------

# ---- helper functions ----
    def test_length(self):
        self.assertEqual(length(Pair(1, Pair(3, Pair(4.5, None)))), 3)
    def test_repr(self):
        self.assertEqual(repr(Pair(1,  None)), 'Pair(1, None)')

# ---- empty ----
    def test_empty(self):
        self.assertEqual(empty_list(), None)

# ---- add ----
    def test_add(self):
        self.assertEqual(add(None, 0, 5), Pair(5, None))
    def test_add2(self):
        self.assertEqual(add(Pair(1, Pair(4, Pair(5, None))), 1, 2), Pair(1, Pair(2, Pair(4, Pair(5, None)))))
    def test_add3(self):
        with self.assertRaises(IndexError):
            add(None, 4, 2)
    def test_add4(self):
        with self.assertRaises(IndexError):
            add(Pair(1, None), -4, -1)
    def test_add6(self):
        self.assertEqual(add(add(empty_list(), 0, 12), 1, 4), Pair(12, Pair(4, None)))

# ---- length ----
    def test_length3(self):
        self.assertEqual(length(None), 0)
    def test_length4(self):
        self.assertEqual(length(Pair( 3, Pair(4, None))), 2)

# ---- get ----
    def test_get(self):
        with self.assertRaises(IndexError):
            get(None, 4)
        with self.assertRaises(IndexError):
            get(Pair(1, None), -1)
        with self.assertRaises(IndexError):
            get(Pair(1, Pair(3, None)), 4)
    def test_get2(self):
        self.assertEqual(get(Pair(0, Pair(1, Pair(2, None))), 0), 0)
    def test_get3(self):
        self.assertEqual(get(Pair(23, Pair(54, Pair(53, None))), 2), 53)
    #def test_get4(self):
        #with self.assertRaises(IndexError):
            #get((None, 3), None)


# ---- set ----
    def test_set(self):
        with self.assertRaises(IndexError):
            set(Pair(1, Pair(3, None)), -2, 5)
        with self.assertRaises(IndexError):
            set(Pair(3, Pair(5, None)), 5, 12)
    def test_set2(self):
        self.assertEqual(set(Pair(3, Pair(5, Pair(12, None))), 1, 23), Pair(3, Pair(23, Pair(12, None))))
    def test_set3(self):
        self.assertEqual(set(Pair(3, None), 0, 5), Pair(5, None))


# ---- remove ----
    def test_remove(self):
        with self.assertRaises(IndexError):
            remove(Pair(1, None), -1)
        with self.assertRaises(IndexError):
            remove(Pair(5, None), 3)
    def test_remove2(self):
        self.assertEqual(remove(Pair(1, Pair(2, None)), 0), (1, Pair(2, None)))
    def test_remove3(self):
        self.assertEqual(remove(Pair(1, None), 0), (1, None))
    def test_remove4(self):
        self.assertEqual(remove(Pair(1, Pair(4, Pair(5, None))), 1), (4, Pair(1, Pair(5, None))))







if __name__ == '__main__':
    unittest.main()
