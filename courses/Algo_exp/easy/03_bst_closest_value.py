# Find closest value to given integer, in bst.

from helpers import BinaryTree


# Awerage: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space
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


# Awerage: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space
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

print(find_closest_value_in_bst(tree.root, 12))
print(find_closest_value_in_bst2(tree.root, 12))
