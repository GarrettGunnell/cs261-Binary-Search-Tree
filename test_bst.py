import unittest
from bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    '''
    Initialization
    '''

    def test_instantiation(self):
        '''
        A Binary Search Tree exists.
        '''
        try:
            BinarySearchTree()
        except NameError:
            self.fail("Could not instantiate BinarySearchTree.")


if __name__ == '__main__':
    unittest.main()
