def check_sort(A, ascending=True):
    """Check if list is sortod O(len(A))"""
    flag = True
    s = 2*int(ascending)-1
    for i in range(len(A)-1):
        if s*A[i] > s*A[i+1]:
            flag = False
            break
    return flag


print(check_sort([0, 0, 2, 2, 3, 4, 7, 22, 25, 28, 43, 43, 54, 88]))
print(check_sort([4,2,7,0,54,43,88,2,3,22,0,43,28,25]))