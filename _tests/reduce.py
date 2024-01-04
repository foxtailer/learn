L = [1, 2, 3, 4, 5]

def fu(a, b):
    return a+b

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

print(reduce(fu, L))