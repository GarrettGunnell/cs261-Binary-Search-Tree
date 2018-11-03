# Binary Search Tree implementation
# Garrett Gunnell

class BinarySearchTree:
    def __init__(self, value = None):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

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
