# Find closest value to given integer, in bst.

import networkx as nx
import matplotlib.pyplot as plt


class BstNode:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
      self.deep = 0

   def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BstNode(data)
                    self.left.deep = self.deep+1
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BstNode(data)
                    self.right.deep = self.deep+1
                else:
                    self.right.insert(data)
        else:
            self.data = data

   def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(f"{self.data}({self.deep})", end=',')
        if self.right:
            self.right.print_tree()


# Function to convert tree to edge list for NetworkX
def add_edges(tree, graph):
    if tree is None:
        return
    if tree.left:
        graph.append((tree.data, tree.left.data))
        add_edges(tree.left, graph)
    if tree.right:
        graph.append((tree.data, tree.right.data))
        add_edges(tree.right, graph)


# RECURSION
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


# LOOP
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
    

tree = BstNode(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(5)
tree.insert(13)
tree.insert(22)
tree.insert(1)
tree.insert(14)
tree.print_tree()
print()

# Convert to edge list
edges = []
add_edges(tree, edges)

# Create graph
G = nx.DiGraph()
G.add_edges_from(edges)

# Draw tree
plt.figure(figsize=(8, 6))
pos = nx.drawing.nx_agraph.graphviz_layout(G, prog="dot")  # Tree layout
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=12, edge_color="gray")
plt.show()
# sudo apt install graphviz graphviz-dev
# pip install --no-binary pygraphviz pygraphviz
# pip install pygraphviz
# pip install pydot


print(find_closest_value_in_bst(tree, 12))
print(find_closest_value_in_bst2(tree, 12))
