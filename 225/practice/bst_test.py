from bst import *
import unittest


class TestCases(unittest.TestCase):
    def test_shit(self):
        tree = BstNode(20, 
                    BstNode(15, 
                        BstNode(12, None, None),
                        BstNode(17, None, None)),
                    BstNode(25,
                        BstNode(22, None, None),
                        BstNode(27, None, None)),
                        )

        tree2 = BstNode(20, 
                    BstNode(12, None, 
                        BstNode(17, None, None)),
                    BstNode(25,
                        BstNode(22, None, None),
                        BstNode(27, None, None)),
                        )
        self.assertEqual(delete(tree, 15), (15, tree2))






if __name__ == '__main__':
    unittest.main()
