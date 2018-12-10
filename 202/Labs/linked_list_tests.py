from linked_list import *
import unittest



class TestList(unittest.TestCase):
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
       # temp_list = set(temp_list, 0, "Bye!")
       # remove(temp_list, 0)

class TestCase(unittest.TestCase):

# ---- helper functions ----
   # def test_length(self):
   #     self.assertEqual(length(Node(1, Node(3, Node(4.5, None)))), 3)
    def test_repr(self):
        self.assertEqual(repr(Node(1,  None)), 'Node(1, None)')

# ---- empty ----
    def test_empty(self):
        self.assertEqual(empty_list(), None)

# ---- add ----
    def test_add(self):
        self.assertEqual(add(None, 0, 5), Node(5, None))
    def test_add2(self):
        self.assertEqual(add(Node(1, Node(4, Node(5, None))), 1, 2), Node(1, Node(2, Node(4, Node(5, None)))))
    def test_add3(self):
        with self.assertRaises(IndexError):
            add(None, 4, 2)
    def test_add4(self):
        with self.assertRaises(IndexError):
            add(Node(1, None), -4, -1)
    def test_add5(self):
        self.assertEqual(add(Node(None, Node(None, Node(None, Node(None, Node(None, Node(None, Node(None, Node(None, Node(None, Node(None, Node(None, Node(None, None)))))))))))), 1, 4), Node(None, Node(4, Node(None, Node(None, Node(None, Node(None, Node(None, Node(None, Node(None, Node(None, Node(None, Node(None, Node(None, None))))))))))))))

    def test_add6(self):
        self.assertEqual(add(add(empty_list(), 0, 12), 1, 4), Node(12, Node(4, None)))

# ---- length ----
    def test_length3(self):
        self.assertEqual(length(None), 0)
    def test_length4(self):
        self.assertEqual(length(Node( 3, Node(4, None))), 2)

# ---- get ----
    def test_get(self):
       # with self.assertRaises(IndexError):
       #     get(None, 4)
        with self.assertRaises(IndexError):
            get(Node(1, None), -1)
        with self.assertRaises(IndexError):
            get(Node(1, Node(3, None)), 4)
    def test_get2(self):
        self.assertEqual(get(Node(0, Node(1, Node(2, None))), 0), 0)
    def test_get3(self):
        self.assertEqual(get(Node(23, Node(54, Node(53, None))), 2), 53)


# ---- set ----
    def test_set(self):
        with self.assertRaises(IndexError):
            set(Node(1, Node(3, None)), -2, 5)
        with self.assertRaises(IndexError):
            set(Node(3, Node(5, None)), 5, 12)
    def test_set2(self):
        self.assertEqual(set(Node(3, Node(5, Node(12, None))), 1, 23), Node(3, Node(23, Node(12, None))))
    def test_set3(self):
        self.assertEqual(set(Node(3, None), 0, 5), Node(5, None))

# ---- remove ----
    def test_remove(self):
        with self.assertRaises(IndexError):
            remove(Node(1, None), -1)
        with self.assertRaises(IndexError):
            remove(Node(5, None), 3)
    def test_remove2(self):
        self.assertEqual(remove(Node(1, Node(4, Node(5, None))), 1), (4, Node(1, Node(5, None))))

    def test_remove3(self):
        self.assertEqual(remove(Node(1, Node(2, None)), 0), (1, Node(2, None)))
    def test_remove4(self):
        self.assertEqual(remove(Node(1, None), 0), ( 1, None))






if __name__ == '__main__':
    unittest.main()
