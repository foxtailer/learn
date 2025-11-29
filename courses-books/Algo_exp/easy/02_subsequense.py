# Find if second array can be created from first one by deleating some items,
# without changing the order of items in first array.


# O(n) time | O(1) space
def subsequence(parent_arr, child_arr):
    """
    >>> subsequence([1,4,5,2,7,8,3,1,12], [4,7,1])
    True
    >>> subsequence([1,4,5,2,7,8,3,1,12], [4,7,13])
    False
    >>> subsequence([1,4,5,2,7,8,3,1,12], [5,4,7])
    False
    """
    parent_pointer = 0
    child_pointer = 0

    while child_pointer < len(child_arr) and parent_pointer < len(parent_arr):
        if child_arr[child_pointer] == parent_arr[parent_pointer]:
            child_pointer += 1
        parent_pointer += 1
    return child_pointer == len(child_arr)


# O(n) time | O(1) space
def subsequence2(parent_arr, child_arr):
    """
    >>> subsequence([1,4,5,2,7,8,3,1,12], [4,7,1])
    True
    >>> subsequence([1,4,5,2,7,8,3,1,12], [4,7,13])
    False
    >>> subsequence([1,4,5,2,7,8,3,1,12], [5,4,7])
    False
    """
    child_pointer = 0

    for value in parent_arr:
        if child_pointer == len(child_arr):
            break
        if child_arr[child_pointer] == value:
            child_pointer += 1
    return child_pointer == len(child_arr)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
