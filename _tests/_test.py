import types


def fibonacci_gen():
    yield 0
    yield 1
    prev_prev, prev = 0, 1

    while True:
        result = prev + prev_prev
        prev_prev, prev = prev, result
        yield result

x = (i*i for i in range(10))
g = fibonacci_gen() #  Return generator
print(type(g))
print(type(x))
print(isinstance(g, types.GeneratorType))
print(isinstance(x, types.GeneratorType))
