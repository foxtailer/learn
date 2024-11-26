last_fn = None


def log(fn):
    def wrapper(a,b):
        print(a)
        print(b)
        result = fn(a,b)
        print(result)
        return result
    
    return wrapper


def round_result(places):
    def decorator(fn):

        def wrapper(a,b):
            return round(fn(a,b), places)
        
        return wrapper
    return decorator


def remember(fn):
    global last_fn
    last_fn = fn
    return last_fn

def green(fn):
    fn.green = True
    return fn

@ green
@ remember
@ log
@ round_result(2)


def add(a,b): return a + b;


last_fn(3.14159, 2.71707)
add(1.222222,2.222222)
print(add.green)
