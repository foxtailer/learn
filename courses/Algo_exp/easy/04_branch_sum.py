# return list with sums of each branch of tree


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


# recursion
# O(n) time | O(n) space (O(log(n)) for recursion n balansed)
def branch_sum(node, sum):
    global result

    if node is None:
        return
    
    if node.left is None and node.right is None:
        result.append(sum + node.data)

    branch_sum(node.left, sum + node.data)
    branch_sum(node.right, sum + node.data)


tree = BinaryTree()
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

# [18, 21, 49, 52, 47]
result = []
branch_sum(tree.root, 0)
print(result)
