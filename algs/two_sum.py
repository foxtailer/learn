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