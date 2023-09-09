def left_bound(A, key):
    left = -1
    right = len(A)

    while right-left > 1:
        middle = (left+right)//2
        if A[middle] < key:
            left = middle
        else:
            right = middle

    return left

def right_bound(A, key):
    left = -1
    right = len(A)

    while right-left > 1:
        middle = (left+right)//2
        if A[middle] <= key:
            left = middle
        else:
            right = middle

    return right

M = [0, 0, 2, 2, 3, 4, 7, 22, 25, 28, 43, 43, 54, 88]
print(left_bound(M,23))
print(right_bound(M,23))