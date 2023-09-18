# a=[[0]*m]*n  => all rowreffer to 1 object

a = [[0]*10 for i in range(10)]
a[1][1] = 1
for row in a:
    print(row)
print()

def king_move(a:list):
    n = 0
    for i in range(1, len(a[0])):
        for j in range(1, len(a[0])):
            if n == 0:
                n+=1
                continue
            a[i][j] = a[i-1][j]+a[i][j-1]
        print(a[i-1])
    print(a[i])

king_move(a)