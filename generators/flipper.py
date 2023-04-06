def flipper_gen(a, b):
    while True:
        yield a
        yield b

flipper = flipper_gen(1, 2)

while True:
    print(next(flipper))