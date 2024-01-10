def nuum_paths(n):
    if n<0:
        return 0
    if n==1 or n==0:
        return 1
    return nuum_paths(n-1) + nuum_paths(n-2) + nuum_paths(n-3)

print(nuum_paths(1))
print(nuum_paths(2))
print(nuum_paths(3))
print(nuum_paths(4))
print(nuum_paths(5))