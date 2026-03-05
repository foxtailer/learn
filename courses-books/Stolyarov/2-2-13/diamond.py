while True:
    try:
        height = int(input('Enter diamond height(positive, odd number): '))
    except:
        print('Height mast be positive, odd number')
    else:
        if height > 0 and height % 2 != 0:
            break
        print('Height mast be positive, odd number')


n = height // 2 + 1


for i in range(1, n + 1):
    print(' ' * (n - i), '*', sep='', end='')
    if i > 1:
        print(' ' * (2 * i - 3), '*', sep='', end='')
    print()
for i in range(n-1, 0, -1):
    print(' ' * (n - i), '*', sep='', end='')
    if i > 1:
        print(' ' * (2 * i - 3), '*', sep='', end='')
    print()

