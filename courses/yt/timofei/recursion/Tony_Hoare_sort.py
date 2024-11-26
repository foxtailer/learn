# Quicksort

def hoar_sort(A):
    if len(A)<=1:
        return

    barrier = A[0]
    L = []
    M = []
    R = []

    for x in A:
        if x<barrier:
            L.append(x)
        elif x==barrier:
            M.append(x)
        else:
            R.append(x)
    
    hoar_sort(L)
    hoar_sort(R)

    k = 0
    for x in L+M+R:
        A[k] = x
        k+=1
    
M = [4,2,7,0,54,43,88,2,3,22,0,43,28,25]
hoar_sort(M)
print(M)