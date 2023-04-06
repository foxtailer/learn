def counter_gen():
    n = 0
    while True:
        yield n
        n += 1

counter = counter_gen()

while True:
    print(next(counter))