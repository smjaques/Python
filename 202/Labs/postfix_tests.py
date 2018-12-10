import unittest
from postfix import *

class TestPostfix(unittest.TestCase):
    def test00_interface(self):
        postfix_calc("1 1 +")

    def test_posfix(self):
        self.assertEqual(postfix_calc('1 2 + 4 *'), 12)

    def test_add_1(self):
        string = "1 2 +"
        self.assertEqual(postfix_calc(string), 3.0)

    def test_subtract_1(self):
        string = "3 5 -"
        self.assertEqual(postfix_calc(string), -2.0)

    def test_subtract_2(self):
        string = "4 5 -"
        self.assertEqual(postfix_calc(string), -1.0)

    def test_multi_1(self):
        string = "5 4 *"
        self.assertEqual(postfix_calc(string), 20.0)

    def test_combine_1(self):
        string = "5 3 + 1 - 6 *"
        self.assertEqual(postfix_calc(string), 42.0)

    def test_divide_1(self):
        string = "6 3 /"
        self.assertEqual(postfix_calc(string), 2.0)

    def test_all_1(self):
        string = "1 2 + 4 *"
        self.assertEqual(postfix_calc(string), 12)



if __name__ == "__main__":
    unittest.main()


