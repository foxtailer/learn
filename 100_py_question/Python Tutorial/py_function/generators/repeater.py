def repeater_gen(value):
    while True:
        yield value

repeat = repeater_gen("Aaa")

while True:
    print(next(repeat))