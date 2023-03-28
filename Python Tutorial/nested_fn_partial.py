# Task 2
# partial(add, 1)(3) -> 4   add is a fn thet takes 2 parameter

def add(a, b):
    return a + b

def partial(fn, x):
    def wrapper(y):
        return fn(x,y)
    return wrapper

print(partial(add, 1)(3))
print(partial(add, 2)(6))
