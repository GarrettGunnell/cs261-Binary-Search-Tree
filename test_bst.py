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

    def test_parent_initially_none(self):
        '''
        A Binary Search Tree has a parent initially set to none
        '''
        bst = BinarySearchTree()
        self.assertEqual(None, bst.parent)

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

    def test_insert_values_under_children(self):
        '''
        If a root already has children, the child will insert instead
        '''
        bst = BinarySearchTree(50)
        child = BinarySearchTree(25)
        insertee = BinarySearchTree(10)
        insertee2 = BinarySearchTree(30)
        bst.insert(child)
        bst.insert(insertee)
        bst.insert(insertee2)
        self.assertEqual(insertee, child.left)
        self.assertEqual(insertee2, child.right)

    def test_inserted_children_point_to_their_parent(self):
        '''
        When a child is inserted, it should point to its parent.
        '''
        bst = BinarySearchTree(50)
        child = BinarySearchTree(25)
        insertee = BinarySearchTree(20)
        bst.insert(child)
        bst.insert(insertee)
        self.assertEqual(bst, child.parent)
        self.assertEqual(child, insertee.parent)

    def test_has_right_child(self):
        bst = BinarySearchTree(50)
        child = BinarySearchTree(75)
        bst.insert(child)
        self.assertEqual(True, bst.has_right_child())

    def test_has_left_child(self):
        bst = BinarySearchTree(50)
        child = BinarySearchTree(25)
        bst.insert(child)
        self.assertEqual(True, bst.has_left_child())

    def test_is_leaf(self):
        bst = BinarySearchTree(50)
        child = BinarySearchTree(25)
        bst.insert(child)
        self.assertEqual(True, child.is_leaf())

    '''
    Finding
    '''

    def test_find(self):
        '''
        A Binary Search Tree can find a node based on its value and return it.
        '''
        bst = BinarySearchTree(50)
        child = BinarySearchTree(20)
        child2 = BinarySearchTree(15)
        child3 = BinarySearchTree(25)
        bst.insert(child)
        bst.insert(child2)
        bst.insert(child3)
        self.assertEqual(child, bst.find(20))
        self.assertEqual(child2, bst.find(15))
        self.assertEqual(child3, bst.find(25))

    def test_find_returns_none_if_no_value_in_tree(self):
        '''
        A Binary Search Tree will return None if the value is not in the tree.
        '''
        bst = BinarySearchTree(50)
        child = BinarySearchTree(25)
        bst.insert(child)
        self.assertEqual(None, bst.find(20))

    '''
    Traversal
    '''

    def test_pre_order(self):
        '''
        A Binary Search Tree can put its contents into a list in preorder.
        '''

        l = [45, 70, 23, 20, 24, 75, 65, 47]
        bst = BinarySearchTree(50)

        for i in l:
            child = BinarySearchTree(i)
            bst.insert(child)

        solution_list = [50, 45, 23, 20, 24, 47, 70, 65, 75]
        test_list = []
        bst.preorder(test_list)
        self.assertEqual(solution_list, test_list)

    def test_post_order(self):
        '''
        A Binary Search Tree can put its contents into a list in postorder.
        '''
        l = [45, 70, 23, 20, 24, 75, 65, 47]
        bst = BinarySearchTree(50)

        for i in l:
            child = BinarySearchTree(i)
            bst.insert(child)

        solution_list = [20, 24, 23, 47, 45, 65, 75, 70, 50]
        test_list = []
        bst.postorder(test_list)
        self.assertEqual(solution_list, test_list)

    def test_in_order(self):
        '''
        A Binary Search Tree can put its contents into a list in order.
        '''
        l = [45, 70, 23, 20, 24, 75, 65, 47]
        bst = BinarySearchTree(50)

        for i in l:
            child = BinarySearchTree(i)
            bst.insert(child)

        solution_list = [20, 23, 24, 45, 47, 50, 65, 70, 75]
        test_list = []
        bst.inorder(test_list)
        self.assertEqual(solution_list, test_list)


if __name__ == '__main__':
    unittest.main()
