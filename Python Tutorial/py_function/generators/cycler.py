def cycler_gen(max):
    n = 0
    while True:
        yield n
        n += 1
        if n == max:
            n = 0

cycler = cycler_gen(15)

while True:
    print(next(cycler))