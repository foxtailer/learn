def power(N, P):
    if P == 0:
        return 1
    print(N,P)
    return (N*power(N, P-1))

print("----", power(2, 4))