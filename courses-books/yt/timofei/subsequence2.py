def lcs(A,B):
    F = [[0]*(len(B)+1) for i in range(len(A)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
        print(F[i-1])
    print(F[i])
    return F[-1][-1]

def gis(a):
    F = [0]*(len(a)+1)
    for i in range(1,len(a)):
        m=0
        for j in range(0,i):
            if a[i]>a[j] and F[j]>m:
                m=F[j]
        F[i]=m+1
    return F[len(a)]


a = [1,2,3,4,5,6,88,8,7,3]
b = [2,3,4,6,8]

print(lcs(a,b))
print(gis(a))