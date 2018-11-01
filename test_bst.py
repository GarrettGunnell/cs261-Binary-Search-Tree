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

    def test_instantiation_with_value(self):
        '''
        A Binary Search Tree has a value
        '''
        fake_value = "FAKE"
        bst = BinarySearchTree(fake_value)
        self.assertEqual(fake_value, bst.value)

    def test_has_left_and_right_initially_none(self):
        '''
        A Binary Search Tree has a left and right initially set to none
        '''
        bst = BinarySearchTree()
        self.assertEqual(None, bst.left)
        self.assertEqual(None, bst.right)

    '''
    Insertion
    '''

    def test_insert_smaller_values_in_left(self):
        '''
        A root inserts smaller values than itself into the left
        '''
        bst = BinarySearchTree(50)
        insertee = BinarySearchTree(25)
        bst.insert(insertee)
        self.assertEqual(insertee, bst.left)

    def test_insert_larger_values_in_right(self):
        '''
        A root inserts larger values than itself into the right
        '''
        bst = BinarySearchTree(50)
        insertee = BinarySearchTree(75)
        bst.insert(insertee)
        self.assertEqual(insertee, bst.right)


if __name__ == '__main__':
    unittest.main()
