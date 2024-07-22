L = [1, 2, 3, 4, 5]

def fu(a, b):
    return a+b

def reduce1(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value



# Reduce (requires functools)
from functools import reduce
print(reduce1(fu, L), reduce(lambda x, y: x + y, L), sep=" = ")
