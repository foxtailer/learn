class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add_child(self, name):
        self.children.append(Node(name))

    def depthFS(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFS(array)
        # array.append("*")
        return array
    
    def dfs(self, array):
        array.append(self.name)
        if self.children:
            for child in self.children:
                array.append(self.name)

node = Node("a")
node.add_child("b")
node.add_child("c")
node.add_child("d")

node.children[0].add_child("e")
node.children[0].add_child("f")

node.children[0].children[1].add_child("i")
node.children[0].children[1].add_child("j")

node.children[2].add_child("g")
node.children[2].add_child("h")
node.children[2].add_child("x")

node.children[2].children[0].add_child("k")

"""
             a
     b       c      d
   e   f          g    h  x
      i j        k
"""

print(node.depthFS([]))