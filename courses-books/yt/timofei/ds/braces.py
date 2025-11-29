import stack

def braces_sequence_correct(s:str):
    '''
    >>> braces_sequence_correct('(([()]))()')
    True
    >>> braces_sequence_correct('([)]')
    False
    >>> braces_sequence_correct('')
    True
    >>> braces_sequence_correct('(')
    False
    >>> braces_sequence_correct(']')
    False
    >>> braces_sequence_correct('f[]')
    False
    >>> braces_sequence_correct('()f')
    False
    >>> braces_sequence_correct('f([])')
    False
    >>> braces_sequence_correct('(fff)')
    True
    '''
    stack.clear()
    braces = {'(':')', '[':']'}

    for brace in s:
        if brace not in "()[]" and stack.is_empty():
            return False
        if brace not in "()[]":
            continue
        
        if brace in '([':
            stack.push(brace)
        else:
            assert brace in ")]", "') or ]' Expected" + str(brace)
            if stack.is_empty():
                return False
            
            left = stack.pop()
            if brace != braces[left]:
                return False
        
    return stack.is_empty()


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(braces_sequence_correct('(([()]))()'))
