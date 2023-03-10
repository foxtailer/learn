def f(a, L = []):
    L.append(a)
    return L

print(f(1))
print(f(2))

def f2(a, L = None):
    if L == None:
        L = []
    L.append(a)
    return L

print(f2(1))
print(f2(2)) 
