last_fn = None


def log_dec(fn):
    def wrapper(a,b):
        print(a)
        print(b)
        result = fn(a,b)
        print(result)
        return result
    
    return wrapper


def round_result_dec(places:int):
    def decorator(fn):
        def wrapper(a,b):
            return round(fn(a,b), places)
        
        return wrapper
    return decorator


def remember_dec(fn):
    global last_fn
    last_fn = fn
    return last_fn


def green_dec(fn):
    fn.green = True
    return fn

@ green_dec
@ remember_dec
@ log_dec
@ round_result_dec(2)
def add(a,b): 
    return a + b


last_fn(3.14159, 2.71707)
add(1.222222,2.222222)
print(add.green)
print(add.__name__)