def gcd(a,b):
    if a == b:
        return a
    elif a>b:
        return gcd((a-b, b))
    else: # a<b  (ghost)
        return gcd(a, b-a)


def gcd2(a,b):
    if b == 0:
        return a
    else:
        return gcd2(b, a%b)
    
def gcd3(a,b):
    return a if b==0 else gcd3(b, a%b)

print(gcd3(3,15)) 
print(gcd(3,15))
print(gcd2(3,15))