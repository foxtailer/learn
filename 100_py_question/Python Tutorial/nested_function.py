def incrementor():
    a = 0
    def inc():
        nonlocal a
        a += 1
        return a
    return inc

fu = incrementor()

print(fu())
print(fu())
print(fu())

