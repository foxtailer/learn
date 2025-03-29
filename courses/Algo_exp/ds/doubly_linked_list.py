import doctest

doctest.testmod()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Keep track of the last node

    # O(1)
    def insert_at_beginning(self, data):
        """
        >>> dll = DoublyLinkedList()
        >>> dll.display()
        []
        >>> dll.insert_at_beginning(1)
        >>> dll.display()
        [1]
        >>> dll.insert_at_end(2)
        >>> dll.display()
        [1<->2]
        """
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            self.head.next = self.head  # Circular link
            self.head.prev = self.head  # Circular link
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node

    # O(1)
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            self.head.next = self.head  # Circular link
            self.head.prev = self.head  # Circular link
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node  # Update tail reference

    # O(1)
    def pop_head(self):
        if not self.head:
            return None  # Empty list
        data = self.head.data
        if self.head == self.tail:  # Only one node
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        return data

    # O(1)
    def pop_tail(self):
        if not self.head:
            return None  # Empty list
        data = self.tail.data
        if self.head == self.tail:  # Only one node
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        return data

    def display(self):
        if not self.head:
            print("[]")
            return
        temp = self.head
        result = []
        while True:
            result.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(f'[{"<->".join(result)}]')
