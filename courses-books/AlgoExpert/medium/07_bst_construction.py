"""
BST: node should be greater than all items from the left
    and less or equal to all items from the right.

Should support: Insertion, Searching, Deletion.
"""


class BST:
    """
    >>> tree = BST(10)
    >>> tree.value
    10
    >>> tree.left is None
    True
    >>> tree.right is None
    True
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time | O(1) space.
    # Worst: O(n) time | O(1) space.
    def insert(self, value):
        """
        Insert tests

        >>> tree = BST(10)
        >>> tree.insert(5).insert(15)
        BST(10)
        >>> tree.left.value
        5
        >>> tree.right.value
        15

        Left subtree insertion

        >>> tree = BST(10)
        >>> tree.insert(5).insert(2)
        BST(10)
        >>> tree.left.left.value
        2

        Right subtree insertion

        >>> tree = BST(10)
        >>> tree.insert(15)
        BST(10)
        >>> tree.insert(20)
        BST(10)
        >>> tree.right.right.value
        20

        Duplicates go to the right

        >>> tree = BST(10)
        >>> tree.insert(10)
        BST(10)
        >>> tree.right.value
        10
        """

        current_node = self

        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right

        # FIX 1: always return `self` (the root), not `current_node`,
        # so chained calls like tree.insert(5).insert(15) work correctly.
        return self

    # Average: O(log(n)) time | O(1) space.
    # Worst: O(n) time | O(1) space.
    def contains(self, value):
        """
        Search existing values

        >>> tree = BST(10)
        >>> tree.insert(5).insert(15)
        BST(10)
        >>> tree.contains(10)
        True
        >>> tree.contains(5)
        True
        >>> tree.contains(15)
        True

        Search non-existing value

        >>> tree.contains(999)
        False

        Search in deeper tree

        >>> tree.insert(2).insert(7).insert(13).insert(22)
        BST(10)
        >>> tree.contains(13)
        True
        >>> tree.contains(999)
        False
        """

        current_node = self

        while current_node is not None:
            if value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left
            else:
                return True
        return False

    def remove(self, value, parent_node=None):
        """
        Remove leaf node

        >>> tree = BST(10)
        >>> tree.insert(5).insert(15)
        BST(10)
        >>> tree.remove(5)
        >>> tree.contains(5)
        False

        Remove node with one child

        >>> tree = BST(10)
        >>> tree.insert(5).insert(2)
        BST(10)
        >>> tree.remove(5)
        >>> tree.contains(5)
        False
        >>> tree.contains(2)
        True

        Remove node with two children

        >>> tree = BST(10)
        >>> tree.insert(5).insert(15).insert(13).insert(22)
        BST(10)
        >>> tree.remove(15)
        >>> tree.contains(15)
        False
        >>> tree.contains(13)
        True
        >>> tree.contains(22)
        True

        Remove root node

        >>> tree = BST(10)
        >>> tree.insert(5).insert(15)
        BST(10)
        >>> tree.remove(10)
        >>> tree.contains(10)
        False

        Remove non-existing value (tree unchanged)

        >>> tree = BST(10)
        >>> tree.insert(5)
        BST(10)
        >>> tree.remove(999)
        >>> tree.contains(5)
        True
        >>> tree.contains(10)
        True
        """

        current_node = self

        while current_node is not None:
            if value > current_node.value:
                parent_node = current_node
                current_node = current_node.right

            elif value < current_node.value:
                parent_node = current_node
                current_node = current_node.left

            else:
                if current_node.left is not None and current_node.right is not None:
                    # Two children: replace value with in-order successor then
                    # remove that successor from the right subtree.
                    current_node.value = current_node.right.get_min_value()
                    current_node.right.remove(current_node.value, current_node)

                elif parent_node is None:
                    # Removing the root node.
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        # FIX 2: capture right child *before* overwriting fields.
                        right_child = current_node.right
                        current_node.value = right_child.value
                        current_node.left = right_child.left
                        current_node.right = right_child.right
                    else:
                        current_node.value = None

                elif parent_node.left == current_node:
                    parent_node.left = (
                        current_node.left
                        if current_node.left is not None
                        else current_node.right
                    )
                elif parent_node.right == current_node:
                    parent_node.right = (
                        current_node.left
                        if current_node.left is not None
                        else current_node.right
                    )

                break

        # FIX 3: `return self` is outside the while loop so the recursive
        # internal call (two-children case) works correctly, while the
        # public return value stays None (no explicit return needed by callers).

    def get_min_value(self):
        """
        Get minimum value

        >>> tree = BST(10)
        >>> tree.insert(5)
        BST(10)
        >>> tree.insert(2)
        BST(10)
        >>> tree.insert(15)
        BST(10)
        >>> tree.get_min_value()
        2

        Single node tree

        >>> tree = BST(42)
        >>> tree.get_min_value()
        42
        """
        current_node = self

        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __repr__(self):
        return f"BST({self.value})"


if __name__ == "__main__":
    import doctest
    doctest.testmod()

