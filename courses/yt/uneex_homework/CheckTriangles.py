"""
Write a subroutine check, which inputs 3 integers and checks if they can form a 
triangle (a=b+c is valid). Subroutine returns 1 if they can. 2 if not, and 0 if 
they were 0, 0, 0. Write a program that calls check and prints 'Y' on 1, or 'N'on 2, 
until check returns 0; then program must exit.


1
2
3
4
5
6
1
4
8
0
0
0

Y
Y
N
"""

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
