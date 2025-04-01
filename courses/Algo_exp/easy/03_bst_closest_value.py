# Find closest value to given integer, in bst.

from treelib import Tree

class BinarySearchTree:
    def __init__(self):
        self.tree = Tree()
        self.root = None

    def insert(self, data):
        if self.root is None:
            # Creating the root node
            self.root = self.tree.create_node(data, data, data=data)
            self.root.left = None
            self.root.right = None
        else:
            self._insert(self.root, data)

    def _insert(self, current_node, data):
        # Insert data to the left
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = self.tree.create_node(data, data, data=data, parent=current_node)
                current_node.left.left = None
                current_node.left.right = None
            else:
                self._insert(current_node.left, data)
        # Insert data to the right
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = self.tree.create_node(data, data, data=data, parent=current_node)
                current_node.right.left = None
                current_node.right.right = None
            else:
                self._insert(current_node.right, data)

    def display(self):
        self.tree.show()


def find_closest_value_in_bst(tree, target):
    return fcvib_helper(tree, target, float("inf"))

def fcvib_helper(tree, target, closest):
    if tree is None:
        return closest
    
    if abs(target - closest) > abs(target - tree.data):
        closest = tree.data

    if target < tree.data:
        return fcvib_helper(tree.left, target, closest)
    elif target > tree.data:
        return fcvib_helper(tree.right, target, closest)
    else:
        return closest


def find_closest_value_in_bst2(tree, target):
    return fcvib_helper(tree, target, float("inf"))

def fcvib_helper(tree, target, closest):
    current_node = tree
    while current_node:
        if abs(target - closest) > abs(target - current_node.data):
            closest = current_node.data
        if target < current_node.data:
            current_node = current_node.left
        elif target > current_node.data:
            current_node = current_node.right
        else:
            break
    return closest


tree = BinarySearchTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(6)
tree.insert(1)
tree.insert(13)
tree.insert(11)
tree.insert(22)
tree.insert(14)

tree.display()

print(find_closest_value_in_bst(tree.root, 12))
print(find_closest_value_in_bst2(tree.root, 12))
