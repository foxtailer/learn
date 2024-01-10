class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node_1 = Node("once")
node_2 = Node("uppon")
node_3 = Node("a")
node_4 = Node("time")

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

def show(li_list):
    while True:
        print(li_list.data)
        if li_list.next == None:
            break
        li_list = li_list.next

show(node_1)