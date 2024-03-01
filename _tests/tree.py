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


root = Node(10)
root.insert(5)
root.insert(15)
root.insert(2)
root.insert(5)
root.insert(13)
root.insert(22)
root.insert(1)
root.insert(14)
root.PrintTree()