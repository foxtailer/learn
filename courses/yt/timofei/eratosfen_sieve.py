N = 100
A = [True] * N  # If index of element are simple number set element to True
#  Imagin that all indexes are simple
A[0] = A[1] = False  # Exept 0 and 1

for i in range(2, N):
    if A[i]:  # if we find simple number. all next numbers with step of i are not simple
        for j in range(i*2, N, i):
            A[j] = False

print(tuple(enumerate(A)))

for i in range(len(A)):
    print(i, "Simple" if A[i] else "Not Simple")