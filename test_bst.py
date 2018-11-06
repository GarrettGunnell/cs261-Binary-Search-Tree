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

    def test_insert_equivalent_values_on_right(self):
        '''
        A root inserts values equal to itself on the right.
        '''

        bst = BinarySearchTree(50)
        insertee = BinarySearchTree(50)
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

    '''
    Deletion
    '''

    def test_delete_leaf(self):
        '''
        A Binary Search Tree can delete a leaf and set its parent's pointer to it to none.
        '''

        bst = BinarySearchTree(50)
        child = BinarySearchTree(25)
        bst.insert(child)
        bst.find(25).delete()
        self.assertEqual(None, bst.left)

    def test_delete_root_with_one_child_on_left(self):
        '''
        A Binary Search Tree with one child will replace itself with its child when deleted.
        '''

        bst = BinarySearchTree(50)
        child = BinarySearchTree(25)
        child2 = BinarySearchTree(20)
        child3 = BinarySearchTree(15)

        bst.insert(child)
        bst.insert(child2)
        bst.insert(child3)
        bst.find(25).delete()

        self.assertEqual(bst.left, child2)

    def test_delete_root_with_one_child_on_right(self):
        '''
        A Binary Search Tree with one child will replace itself with its child when deleted.
        '''

        bst = BinarySearchTree(50)
        child = BinarySearchTree(75)
        child2 = BinarySearchTree(80)
        child3 = BinarySearchTree(85)

        bst.insert(child)
        bst.insert(child2)
        bst.insert(child3)
        bst.find(75).delete()

        self.assertEqual(bst.right, child2)

    def test_find_minimum(self):
        '''
        A Binary Search Tree can find its minimum value.
        '''

        bst = BinarySearchTree(50)
        child = BinarySearchTree(25)
        child2 = BinarySearchTree(20)
        child3 = BinarySearchTree(15)
        child4 = BinarySearchTree(17)

        bst.insert(child)
        bst.insert(child2)
        bst.insert(child3)
        bst.insert(child4)

        self.assertEqual(child3, bst.find_minimum())

    def test_find_successor(self):
        '''
        A Binary Search Tree can find a node to replace itself.
        '''
        values = [50, 150, 25, 10, 30, 75, 70, 80, 125, 110, 130, 175, 160, 200]
        bst = BinarySearchTree(100)
        for i in values:
            bst.insert(BinarySearchTree(i))

        self.assertEqual(bst.find(50).find_successor(), bst.find(70))


    def test_delete_root_with_two_children(self):
        '''
        A Binary Search Tree with two children will find a successor to replace itself when deleted.
        '''

        values = [50, 150, 25, 10, 30, 75, 70, 80, 125, 110, 130, 175, 160, 200]
        bst = BinarySearchTree(100)
        for i in values:
            bst.insert(BinarySearchTree(i))

        bst.find(50).delete()
        bst.find(150).delete()
        self.assertEqual(bst.find(70), bst.left)
        self.assertEqual(bst.find(160), bst.right)


if __name__ == '__main__':
    unittest.main()
