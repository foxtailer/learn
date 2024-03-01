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

def branch_sum(root):
    sums = []
    calculate_bs(root, 0, sums)
    return sums

def calculate_bs(node, running_sum, sums):
    if node is None:
        return
    
    new_running_sum = running_sum + node.data
    if node.left is None and node.right is None:
        sums.append(new_running_sum)
        return
    
    calculate_bs(node.left, new_running_sum, sums)
    calculate_bs(node.right, new_running_sum, sums)

root = Node(10)
root.insert(5)
root.insert(15)
root.insert(2)
root.insert(5)
root.insert(13)
root.insert(22)
root.insert(1)
root.insert(14)

print(branch_sum(root))