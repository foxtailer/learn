# def fibo(n):
#     if n==1 or n==0:
#         return n
#     return fibo(n-1) + fibo(n-2)

# 

def fibo(n, memo):
    if n==0 or n==1:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibo(n-2, memo) + fibo(n-1, memo)
        return memo[n]
    
print(fibo(10, {}))
