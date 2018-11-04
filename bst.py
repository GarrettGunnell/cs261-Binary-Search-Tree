# Binary Search Tree implementation
# Garrett Gunnell


class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def is_leaf(self):
        return self.right is None and self.left is None

    def insert(self, child):
        if child.value > self.value:
            if self.right is None:
                self.right = child
                self.right.parent = self
            else:
                self.right.insert(child)
                self.right.parent = self
        else:
            if self.left is None:
                self.left = child
                self.left.parent = self
            else:
                self.left.insert(child)
                self.left.parent = self

    def find(self, value):
        if value is self.value:
            return self
        elif self.is_leaf():
            return None
        elif value > self.value:
            return self.right.find(value)
        elif value < self.value:
            return self.left.find(value)

    def preorder(self, list_):
        list_.append(self.value)

        if self.has_left_child():
            self.left.preorder(list_)
        if self.has_right_child():
            self.right.preorder(list_)

    def postorder(self, list_):
        if self.has_left_child():
            self.left.postorder(list_)
        if self.has_right_child():
            self.right.postorder(list_)
        list_.append(self.value)

    def inorder(self, list_):
        if self.has_left_child():
            self.left.inorder(list_)

        list_.append(self.value)

        if self.has_right_child():
            self.right.inorder(list_)
