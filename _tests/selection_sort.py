def select_sort(A):
    """
    >>> select_sort([1,3,2])
    [1, 2, 3]
    """
    N = len(A)
    for start in range(N):
        selected = None
        for i in range(start+1, N):
            if A[i]<A[start]:
                selected=i
        if selected:
            A[start],A[selected]=A[selected],A[start]
    return A


if __name__ == "__main__":
    import doctest
    print(select_sort([4,3,6]))
    doctest.testmod()