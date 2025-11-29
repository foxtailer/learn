def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def trial_division(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

#####################################

n = 100

for i in range(1, n + 1):
    flag = True

    for j in range(2, i):
        if i % j == 0:
            flag = False
    
    if flag:
        print(f'{i} is prime.')

#####################################
        

n = 100

for i in range(1, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:  #  No break
        print(i)