import stack

def rpn(A:list):
    """
    >>> rpn([2,3,'+'])
    5
    >>> rpn([3,3,'+'])
    6
    >>> rpn([2,7,'+',5,'*'])
    45
    >>> rpn([2,7,5,'*','+'])
    37
    """
    stack.clear()

    for token in A:
        if type(token) == type('gg'):
            stack.push(eval(f"{stack.pop()}{token}{stack.pop()}"))
        else:
            stack.push(token)

    return stack.pop()    


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(rpn([2,7,5,'*','+']))
