def deco_generator(period):
    def decorator(fn):
        def wrapper(a,b):
            return round(fn(a,b),period)
        return wrapper
    return decorator

@deco_generator(2)
def add(a,b):
    return a+b

print(add(2.49538, 2.1538))
