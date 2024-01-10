import time
def fibo_gen():
    yield 0
    yield 1
    
    a,b = 0,1
    while True:
        a,b = b, a + b
        yield a + b

fn = fibo_gen()

while True:
    time.sleep(1)
    print(next(fn))
