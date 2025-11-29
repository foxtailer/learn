# return list with sums of each branch of tree

from helpers import BinaryTree


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
