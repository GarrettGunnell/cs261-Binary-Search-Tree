# Binary Search Tree implementation
# Garrett Gunnell

class BinarySearchTree:
    def __init__(self, value = None):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def is_leaf(self):
        return self.right == None and self.left == None

    def insert(self, child):
        if child.value > self.value:
            if self.right == None:
                self.right = child
                self.right.parent = self
            else:
                self.right.insert(child)
                self.right.parent = self
        else:
            if self.left == None:
                self.left = child
                self.left.parent = self
            else:
                self.left.insert(child)
                self.left.parent = self

    def find(self, value):
        if value == self.value:
            return self
        elif self.is_leaf():
            return None
        elif value > self.value:
            return self.right.find(value)
        elif value < self.value:
            return self.left.find(value)
