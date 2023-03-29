# Task 3
# @ cashe
# def add(a,b): return a + b;
# add(3, 3) -> 6
# add(4, 8) -> 6
# add(5, 3) -> 6

def cashe(fn):
    temp = None
    def wrapper(x, y):
        nonlocal temp
        if temp:
            return temp
        else:
            temp = fn(x, y)
            return temp
    return wrapper

@ cashe
def add(a, b): return a + b;

print(add(3, 2))
print(add(4, 5))

print("*******")
#///////////////////////////////

def cache2(func):
    value = None
    def wrapper(x, y):
        nonlocal value
        if value == None:
            value = func(x, y)
        return value
    return wrapper

@cache2
def add2(x, y):
    return x+y

print(add2(3, 5))
print(add2(1, 2))
print(add2(2, 1))