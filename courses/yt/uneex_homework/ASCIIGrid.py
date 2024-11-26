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
    