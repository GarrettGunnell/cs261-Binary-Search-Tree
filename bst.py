#Binary Search Tree implementation
#Garrett Gunnell

class BinarySearchTree:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, child):
        if child.value > self.value:
            self.right = child
        else:
            self.left = child
