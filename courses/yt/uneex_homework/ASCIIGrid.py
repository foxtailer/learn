"""
Wrirte a program that inputs ordinals M an N, and outputs MxN grid made with «+» and «-». 
You should write a macro that accepts three parameters: a number of cells and two characters, 
and outputs a line like this:

printline 4, '+', '-'

→
+-+-+-+-+


3
4

+-+-+-+
| | | |
+-+-+-+
| | | |
+-+-+-+
| | | |
+-+-+-+
| | | |
+-+-+-+
"""

def printline(n, char='-', sep='+'):
    """
    >>> printline(4, '-', '+')
    +-+-+-+-+
    """
    char = str(char)
    sep = str(sep)
    print(f'{sep}{sep.join([char]*n)}{sep}')


def printcell(n):
     print(f'{"|"}{"|".join([" "]*n)}{"|"}')


def main():
    try:
        x = int(input('x: '))
        y = int(input('y: '))
    except:
        print('x, y must be int.')
        return

    # Simple
    for i in range(y):
        printline(x)
        printcell(x)
    printline(x)

if __name__ == '__main__':
    main()
    