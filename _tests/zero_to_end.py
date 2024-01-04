some_list = [1,5,3,0,8,7,0,2,0]

def zero_to_end(L:list) -> list:
    """Push all zeros in L to the and of list"""

    start = 0
    stop = len(L)-1

    while start < stop:
        if L[start] == 0:
            if L[stop] == 0:
                stop -= 1
            else:
                L[start], L[stop] = L[stop], L[start]
                start += 1
                stop -= 1
        else:
            start += 1

    return L

print(zero_to_end(some_list))
print(sorted(some_list, key=lambda x: x==0))