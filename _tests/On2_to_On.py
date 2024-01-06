def find_duplicates(array):
    """
    >>> find_duplicates([1,2,1,3])
    True
    >>> find_duplicates([1,2,3])
    False
    """
    for i in range(len(array)):
        for j in range(len(array)):
            if i!=j and array[i]==array[j]:
                return True
    return False


def find_duplicates_2(array):
    """
    >>> find_duplicates_2([1,2,1,3])
    True
    >>> find_duplicates_2([1,2,3])
    False
    """
    duplicates = [0]*(max(array)+1)
    for i in range(len(array)):
        if duplicates[array[i]] == 1:
            return True
        else:
            duplicates[array[i]] = 1 
    return False

if __name__ == "__main__":
    import doctest
    print(find_duplicates([1,2,1,3,5]))
    print(find_duplicates_2([1,2,1,3,5]))
    doctest.testmod(verbose=True)