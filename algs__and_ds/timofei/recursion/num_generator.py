def num_gen(N:int, M:int, prefix=None):
    if M == 0:
        print(prefix)
        return
    prefix = prefix or []
    for digit in range(N):
        prefix.append(digit)
        num_gen(N, M-1, prefix)
        prefix.pop()

def gen_bin(N, prefix=""): #
    if N == 0:
        print(prefix)
    else:
        gen_bin(N-1, prefix + "0")
        gen_bin(N-1, prefix + "1")

gen_bin(5)
num_gen(4, 3)