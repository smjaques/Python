
import unittest
from hash_table_chaining import *
class TestCases(unittest.TestCase):

    def test_HashObject(self):
        hash_table = HashTable([[(1, 0)], [2, 1]], 2, 2, 0)
        hash_table2 = HashTable([[(3, 0)], [4, 1]], 2, 2, 0)
        hash_table3 = HashTable([[(1, 0)], [2, 1]], 2, 2, 0)
        self.assertEqual(hash_table, hash_table3)
        self.assertEqual(repr(hash_table), "HashTable([[(1, 0)], [2, 1]], 2, 2, 0)")
        self.assertEqual(hash_table.list, [[(1, 0)], [2, 1]])


    def test_empty_hash_table(self):
        hash_table = HashTable([[None], [None], [None], [None], [None],
                                [None], [None], [None]], 0, 8, 0)
        self.assertEqual(empty_hash_table(), hash_table)

    def test_get(self):
        hash_table = HashTable([[(1, 0)], [(2, 1)], [(3, 2)], [(4, 3)], [(5, 4)],
                                [(6, 5)], [(7, 6)], [(8, 7)]], 8, 8, 0)
        hash_table2 = HashTable([[None], [None], [None], [None], [None],
                                [None], [None], [None]], 0, 8, 0)
        self.assertEqual(get(hash_table, 2), 3)
        self.assertRaises(LookupError, get, hash_table2, 5)

    def test_remove(self):
        hash_table = HashTable([[(1, 0)], [(2, 1)], [(3, 2)], [(4, 3)], [(5, 4)],
                                [(6, 5)], [(7, 6)], [(8, 7)]], 8, 8)
        hash_table2 = HashTable([[(1, 0)], [(2, 1)], [(3, 2)], [], [(5, 4)],
                                [(6, 5)], [(7, 6)], [(8, 7)]], 7, 8)
        hash_table3 = HashTable([[(1, 0)], [(2, 1)], [(3, 2)], [(4, 3)], [(5, 4)],
                                [(6, 5)], [(7, 6)], [(8, 7), (9, 8)]], 9, 8)
        hash_table4 = HashTable([[(1, 0)], [(2, 1)], [(3, 2)], [(4, 3)], [(5, 4)],
                                [(6, 5)], [(7, 6)], [(9, 8)]], 8, 8)
        hash_table5 = HashTable([[None], [None], [None], [None], [None],
                                [None], [None], [None]], 0, 8)
        self.assertEqual(remove(hash_table, 3), hash_table2)
        self.assertEqual(remove(hash_table3, 7), hash_table4)
        self.assertRaises(LookupError, remove, hash_table5, 2)

    def test_size(self):
        hash_table = HashTable([[(1, 0)], [(2, 1)], [(3, 2)], [(4, 3)], [(5, 4)],
                                [(6, 5)], [(7, 6)], [(8, 7)]], 8, 8)
        self.assertEqual(size(hash_table), 8)

    def test_load_factor(self):
        hash_table = HashTable([[(1, 0)], [(2, 1)], [(3, 2)], [(4, 3)], [(5, 4)],
                                [(6, 5)], [(7, 6)], [(8, 7)]], 8, 8)
        hash_table2 = HashTable([[(1, 0)], [(2, 1)], [(3, 2)], [(4, 3)], [(5, 4)],
                                [(6, 5)], [(7, 6)], [(8, 7), (9, 8)]], 9, 8)
        self.assertEqual(load_factor(hash_table), 1)
        self.assertEqual(load_factor(hash_table2), 1.125)

    def test_collisions(self):
        hash_table = HashTable([[(1, 0)], [(2, 1)], [(3, 2)], [(4, 3)], [(5, 4)],
                                [(6, 5)], [(7, 6)], [(8, 7)]], 8, 8)
        hash_table2 = HashTable([[(1, 0)], [(2, 1)], [(3, 2)], [(4, 3)], [(5, 4)],
                                 [(6, 5)], [(7, 6)], [(8, 7), (9, 8)]], 9, 8, 1)
        hash_table3 = HashTable([[(1, 0)], [(2, 1), (2, 3)], [(3, 2)], [(4, 3)], [(5, 4)],
                                 [(6, 5)], [(7, 6)], [(8, 7), (9, 8)]], 9, 8, 2)
        hash_table4 = HashTable([[(1, 0)], [(2, 1), (2, 3)], [(3, 2)], [(4, 3)], [(5, 4)],
                                 [(6, 5)], [(7, 6)], [(8, 7), (9, 8), (6, 99)]], 10, 8, 3)
        hash_table5 = HashTable([[None], [None], [None], [None], [None],
                                 [None], [None], [None]], 0, 8)
        self.assertEqual(collisions(hash_table), 0)
        self.assertEqual(collisions(hash_table2), 1)
        self.assertEqual(collisions(hash_table3), 2)
        self.assertEqual(collisions(hash_table4), 3)
        self.assertEqual(collisions(hash_table5), 0)

    def test_insert(self):
        hash_table = empty_hash_table()
        hash_table2 = HashTable([[None], [(1,1)], [None], [None], [None],
                                [None], [None], [None]], 1, 8)
        self.assertEqual(insert(hash_table, 1, 1), hash_table2)
        self.assertEqual(insert(hash_table2, 1, 1), hash_table2)

    def test_insert_collision(self):
        hash_table2 = HashTable([[(1, 0)], [(2, 1), (2, 3)], [(3, 2)], [(4, 3)], [(5, 4)],
                                 [(6, 5)], [(7, 6)], [(8, 7), (9, 8)]], 9, 8, 2)
        hash_table3 = HashTable([[(1, 0)], [(2, 1), (2, 3)], [(3, 2)], [(4, 3)], [(5, 4)],
                                 [(5, 5)], [(7, 6)], [(8, 7), (9, 8)]], 9, 8, 3)
        hash_table4 = HashTable([[(1, 0)], [(2, 1), (2, 3)], [(3, 2)], [(4, 3)], [(5, 4)],
                                 [(5, 5)], [(7, 6)], [(7, 7), (9, 8)]], 9, 8, 4)
        self.assertEqual(insert(hash_table2, 5, 5), hash_table3)
        self.assertEqual(insert(hash_table2, 7, 7), hash_table4)

    def test_insert_rehash(self):
        hash_table = HashTable([[(0,0), (1, 1), (2, 2)], [None]], 3, 2, 2)
        hash_table2 = HashTable([[(0,0)], [(1,1)], [(2, 2)], [(3, 3)]], 4, 4, 0)

        self.assertEqual(insert(hash_table, 3, 3), hash_table2)

    def test_insert_more(self):
        hash_table = HashTable([[(1, 0)], [(2, 3)], [(3, 2)], [(4, 3)], [(5, 4)],
                   [(6, 5)], [(7, 6)], [(8, 7), (9, 8)]], 9, 8, 1)
        hash_table2 = HashTable([[(1, 0)], [(2, 3), (9, 1)], [(3, 2)], [(4, 3)], [(5, 4)],
                   [(6, 5)], [(7, 6)], [(8, 7), (9, 8)]], 10, 8, 2)
        hash_table3 = HashTable([[(1, 0)], [(2, 3), (9, 3)], [(3, 2)], [(4, 3)], [(5, 4)],
                   [(6, 5)], [(7, 6)], [(8, 7), (9, 8)]], 10, 8, 2)
        hash_table4 = HashTable([[(1, 0)], [(2, 3), (9, 3), (8, 1)], [(3, 2)], [(4, 3)], [(5, 4)],
                   [(6, 5)], [(7, 6)], [(8, 7), (9, 8)]], 11, 8, 3)
        self.assertEqual(insert(hash_table, 1, 9), hash_table2)
        self.assertEqual(insert(hash_table3, 1, 8), hash_table4)


if __name__ == '__main__':
    unittest.main()
