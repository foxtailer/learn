a = [0, 1, 2, 3, 4, 5]

def left_shift(a):
    tmp = a[0]
    for i in range(len(a)-1):
        a[i] = a[i+1]
    a[-1] = tmp

def right_shift(a):
    tmp = a[-1]
    for i in range(len(a)-1, 0, -1):
        a[i] = a[i-1]
    a[0] = tmp

print(a)
left_shift(a)
print(a)

a = [0, 1, 2, 3, 4, 5]

print(a)
right_shift(a)
print(a)