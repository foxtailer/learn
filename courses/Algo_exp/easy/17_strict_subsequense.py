def strict_subsequence(parent_arr, child_arr):
    """
    >>> strict_subsequence([1,2,3,4,5,6], [1,2,3])
    True
    >>> strict_subsequence([1,2,3,4,5,6], [3,4,5])
    True
    >>> strict_subsequence([1,2,3,4,5,6], [1,3,4])
    False
    >>> strict_subsequence([1,2,3,4,5,6], [3,5,6])
    False
    """
    parent_len = len(parent_arr)
    child_len = len(child_arr)
    
    # Iterate through parent_arr, checking for a contiguous match starting at each position
    for i in range(parent_len - child_len + 1):
        # Check if a slice of parent_arr matches child_arr
        if parent_arr[i:i + child_len] == child_arr:
            return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
