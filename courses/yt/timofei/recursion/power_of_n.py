def power(N, P):
    if P == 0:
        return 1
    print(N,P)
    return (N*power(N, P-1))

print("----", power(2, 4))

def fast_power(a, n):
    if n == 0:
        return 1
    elif n%2 == 1:  # even
        return fast_power(a, n-1)*a
    else:  # odd
        return fast_power(a**2, n//2)