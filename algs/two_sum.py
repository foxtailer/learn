# Task: Find 2 elenents in LIST whose summ = SUMM
LIST = [3, 5, -4, 8, 11, -1, 6, 4]
SUMM = 10


# 1
result = []
for i in LIST:
    for j in LIST:
        if i + j == 10\
        and LIST.index(i) != LIST.index(j)\
        and (i, j) not in result\
        and (j, i) not in result:
            result.append((i, j))
print(result)

# 1.2
result = []
for i in range(len(LIST) - 1):
    first_num = LIST[i]
    for j in range(i + 1, len(LIST)):
        second_num = LIST[j]
        if first_num + second_num == SUMM:
            result.append((first_num, second_num))
print(result)

# 2
result = []
for i in LIST:
    j = SUMM - i
    if j in LIST\
    and LIST.index(i) != LIST.index(j)\
    and (i, j) not in result\
    and (j, i) not in result:
        result.append((i, j))
print(result)

# 3
result = []
temp = []
for i in LIST:
    j = SUMM - i
    if j not in temp:
        temp.append(i)
    else:
        result.append((i, j))
print(result)

# 4
result = []
S_LIST = sorted(LIST)
L = 0
R = len(S_LIST) - 1
while L < R:
    curent_sum = S_LIST[L] + S_LIST[R]
    if curent_sum  == SUMM:
        result.append((S_LIST[L], S_LIST[R]))
        L += 1
        R -= 1
    elif curent_sum < SUMM:
        L += 1
    elif curent_sum > SUMM:
        R -= 1
print(result)