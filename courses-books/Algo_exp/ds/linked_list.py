# manual linked list

import doctest


doctest.testmod()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # O(1)
    def insert_at_beginning(self, data):
        """
        >>> ll = LinkedList()
        >>> ll.display()
        []
        >>> ll.insert_at_beginning(1)
        >>> ll.display()
        [1]
        >>> ll.insert_at_end(2)
        >>> ll.display()
        [1->2]
        """ 
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node  # Update head

    # O(n)
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node  # Add to last node

    # O(1) at head, O(n) at arbitrary position
    def delete_by_value(self, value):
        temp = self.head

        # If head holds the value
        if temp and temp.data == value:
            self.head = temp.next
            return

        # Search for the node to delete
        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next  # Remove reference to node

    def display(self):
        temp = self.head
        result = []
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        print(f'[{"->".join(result)}]')
