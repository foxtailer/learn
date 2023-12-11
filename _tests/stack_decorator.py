
def green(fn):
    fn.green = True
    return fn

global_var = None

def remember(fu):
    global global_var
    global_var = fu
    return fu

def round_result(period):
    def decorator(fn):
        def wrapper(a,b):
            return round(fn(a,b),period)
        return wrapper
    return decorator

def log(fn):
    def wrapper(a,b):
        print(a)
        print(b)
        result = fn(a,b)
        return result
    return wrapper



@log
@round_result(2)
@remember
@green
def add(a,b):
    return a+b

# add.green = atribute atributrerror
# fn (3.134, 2.32552) not rounded
# add
# add

print(add.green)