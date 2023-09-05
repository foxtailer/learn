def add(a, b): return a + b

def reduce(fn, *terms, initial=0):
    if terms:
        return fn(terms[0], reduce(fn, *terms[1:], initial=0))
    else:
        return initial

print(reduce(add, 1,2,3,4))