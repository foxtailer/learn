# N - amount of items, M - bag size
F = [[0]*(N+1) for i in range(M+1)]

for i in range(1,N):
    for k in range(1, M):
        if m[i]<=k:
            F[k][i] = max(F[k][i-1],v[i] + F[k-m[i]][i-1])
        else:
            F[k][i] = F[k][i-1]