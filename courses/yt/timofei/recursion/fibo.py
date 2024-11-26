a,b = 0,1
while a < 33:
    print(a)
    a, b = b, a+b

print("****")

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibo(n -1) + fibo(n - 2))
    
for i in range(20):
    print(fibo(i))
