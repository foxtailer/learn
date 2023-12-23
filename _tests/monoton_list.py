L1 = [1,3,5,6,7]
L2 = [3,1,8,2]
L3 = [9,7,5,3,2,1]

def monoton_check(l:list):
    up = True
    down = True
    for i in range(len(l)-1):
        if l[i]<l[i+1]:
            down = False
        if l[i]>l[i+1]:
            up = False
    return up or down

print(monoton_check(L1))
print(monoton_check(L2))
print(monoton_check(L3))
