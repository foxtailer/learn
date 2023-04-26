def array_search(A:list, N:int, x:int):
    """make search of x in list A, from
    0 to N - 1. Return index of x if x in
    A and -1 if not.
    if x in A more then one time, return index of first x
    """
    for i in range(N):
        if A[i] == x:
            return i
    return -1

def test():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print("test1 ++")
    else:
        print("test1 --")

    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print("test2 ++")
    else:
        print("test2 --")

    A3 = [10, 20, 30, 10, 10]
    m = array_search(A3, 5, 10)
    if m == 0:
        print("test3 ++")
    else:
        print("test3 --")

test()