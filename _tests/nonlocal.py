def double():
    b = 2
    def triple():
        # b*3  work well cose after program cant find b in triple she go to double
        nonlocal b
        b = b*3
        return b
    return triple



d = double()
print(d())