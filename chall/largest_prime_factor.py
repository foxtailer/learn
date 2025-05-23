x = 806515533049393


# Too slow -----------------
def find_factors(x):
    result = []
    for i in range(2, x+1):
        if x % i == 0:
            result.append(i)
    return result
# --------------------------


# MemoryError -------------
'''
A = [True] * x  
A[0] = A[1] = False

for i in range(2, x):
    if A[i]: 
        for j in range(i*2, x, i):
            A[j] = False

for i in range(len(A) - 1, -1, -1):
    if A[i] and x % i == 0:
        print(i)
        break
'''
# -------------------------

def largest_prime_factor(n):
    i = 2
    last_factor = 1
    while i * i <= n:
        if n % i == 0:
            last_factor = i
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        last_factor = n  # n is prime
    return last_factor


print(largest_prime_factor(x))
