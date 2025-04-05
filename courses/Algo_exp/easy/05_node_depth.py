# find sum of depth of each node in tree

from helpers import BinaryTree


# O(n) time | O(h) space h - height of tree
def node_depth(root):
    result = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        node_info = stack.pop()
        node = node_info["node"]
        depth = node_info["depth"]
        
        if node == None:
            continue

        result += depth
        stack.append({"node": node.left, "depth": depth+1})
        stack.append({"node": node.right, "depth": depth+1})
    return result


# O(n) time | O(h) space h - height of tree
def node_depth2(root, depth=0):
    if root is None:
        return 0
    
    return depth + node_depth2(root.left, depth + 1) + node_depth2(root.right, depth + 1)


tree = BinaryTree()
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(5)
tree.insert(13)
tree.insert(22)
tree.insert(1)
tree.insert(14)
tree.insert(3)
tree.display()

print(node_depth(tree.root))
print(node_depth2(tree.root))
