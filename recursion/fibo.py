def fibo(n):
    if n < 0:
        print(0)
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        result = fibo(n -1) + fibo(n -2)
        print(result)
        return result

fibo(7)
