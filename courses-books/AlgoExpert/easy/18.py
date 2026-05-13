def kadaneAlgorithm(A: list[int]) -> int:
    """
    >>> kadaneAlgorithm([1,2,3,4,5,6])
    21
    >>> kadaneAlgorithm([-2,1,-3,4,-1,2,1,-5,4])
    6
    """
    
    max_current = max_global = A[0]
    
    for num in A[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
        
    return max_global


if __name__ == "__main__":
    import doctest
    doctest.testmod()
