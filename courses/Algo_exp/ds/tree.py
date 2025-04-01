# trees
# req: pip install treelib
#
# bst
# Every node can have zero, one, or two child nodes.
# The topmost node in the tree is called the root.
# Except for the root, every node in the tree has exactly one parent.
# Each left or right child of a node itself forms a binary tree.


from treelib import Tree


# Create tree using treelib
tree = Tree()
tree.create_node(10, "10")  # Root (name, identifier)
tree.create_node(5, "5", parent="10")
tree.create_node(15, "15", parent="10")
tree.create_node(2, "2", parent="5")
tree.create_node(0, "0", parent="2")
tree.create_node(5, "5'", parent="5")  # Duplicate 5 with a unique ID
tree.create_node(13, "13", parent="15")
tree.create_node(22, "22", parent="15")
tree.create_node(1, "1", parent="2")
tree.create_node(14, "14", parent="13")

# Display tree in text format
tree.show()

tree.all_nodes()
tree.children('15')  # [Node(tag=13, identifier=13, data=None), Node(tag=22, identifier=22, data=None)]