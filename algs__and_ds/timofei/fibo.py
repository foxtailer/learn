n = 100
fib = [0,1] + [0]*(n-1)
for i in range(2,n+1):
    fib[i] = fib[i-1]+fib[i-2]
print(fib[-1])
