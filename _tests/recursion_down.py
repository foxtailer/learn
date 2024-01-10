def factorial(n, i=1, product=1):
    if i>n:
        return product
    else:
        return factorial(n, i+1, product*i)

print(factorial(5))