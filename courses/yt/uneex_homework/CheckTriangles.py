def check():
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    triangle = [a, b, c]
    triangle.sort()

    if triangle[2] == triangle[0] == triangle[1] == 0:
        return 0
    elif triangle[2] == triangle[0] + triangle[1]:
        return 1
    else:
        return 2


while True:
    result = check()

    if result == 1:
        print('Y')
    elif result == 0:
        break
    else:
        print('N')
