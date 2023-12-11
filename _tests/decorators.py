# @decorator
# def fn(...):
#     ...

# -> equal
# def fn(...):...
# fn = decorator(fn)

# @a
# @b
# def fn(...):...
# fn = a(b(fn))

#! every object in python have name space


def green(fn):
    fn.green = True
    return fn

@green
def add(a,b):
    return a+b

print(add.green)
print()

###########################

global_var = None

def sever(fu):
    global global_var
    global_var = fu
    return fu

@sever
def add2(a,b):
    return a+b

print(global_var(1,3), add2(1,3),add.green)

##################

def two_float(fn):
    def wrapper(a,b):
        a = float(a)
        b = float(b)
        return fn(a,b)
    return wrapper

@two_float
def add(a,b):
    return a+b

print(add(2,2))

##################

def round2(fn):
    def wrapper(a,b):
        result = round(fn(a,b))
        return result
    return wrapper

@round2
def add4(a,b):
    return a+b

print(add4(3.7, 1.2))