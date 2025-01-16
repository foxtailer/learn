def find(x, A):
    for i in A:
        if i == x:
            return True
    return False

def generate_permutations(N, M=-1, prefix=None):
    """все варианты n чисел в m позициях"""
    M = M if M != -1 else N
    prefix = prefix or []

    if M == 0:
        print(*prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

generate_permutations(5, 3)
