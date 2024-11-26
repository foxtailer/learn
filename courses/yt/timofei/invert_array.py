def invert_array(a:list, n:int):
    """reverse array 0 to n-1
    """
    # b = [0]*n
    # for i in range(n):
    #     b[i] = a[n-1-i]
    # return b
    
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i] 

def test():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    invert_array(A1, 5)
    print(A1)
    if A1 == [5,4,3,2,1]:
        print("test1 ++")
    else:
        print("test1 --")
    
    A2 = [0, 0, 0, 1]
    print(A2)
    invert_array(A2, 4)
    print(A2)
    if A2 == [1, 0, 0, 0]:
        print("test2 ++")
    else:
        print("test2 --")
test()