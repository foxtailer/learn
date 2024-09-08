class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
      self.deep = 0

   def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                    self.left.deep = self.deep+1
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                    self.right.deep = self.deep+1
                else:
                    self.right.insert(data)
        else:
            self.data = data

   def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(f"{self.data}({self.deep})", end=','),
        if self.right:
            self.right.PrintTree()

# RECURSION
# def findClosestValueInBst(tree, target):
#     return fcvib_helper(tree, target, float("inf"))

# def fcvib_helper(tree, target, closest):
#     if tree is None:
#         return closest
#     if abs(target - closest) > abs(target - tree.data):
#         closest = tree.data
#     if target < tree.data:
#         return fcvib_helper(tree.left, target, closest)
#     elif target > tree.data:
#         return fcvib_helper(tree.right, target, closest)
#     else:
#         return closest


# LOOP
def findClosestValueInBst(tree, target):
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
    

root = Node(10)
root.insert(5)
root.insert(15)
root.insert(2)
root.insert(5)
root.insert(13)
root.insert(22)
root.insert(1)
root.insert(14)

print(findClosestValueInBst(root, 12))