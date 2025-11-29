class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def heigh_tree(A):
    if (A==None):
        return 0
    else:
        ldepth = heigh_tree(A.left)   # first step
        rdepth = heigh_tree(A.right)  # second

        if ldepth > rdepth: # third
            return 1+ldepth
        else:
            return 1+rdepth

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
root.right.right = Node(6)

print(heigh_tree(root))
