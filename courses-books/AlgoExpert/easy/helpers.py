from treelib import Tree


class BinaryTree:
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