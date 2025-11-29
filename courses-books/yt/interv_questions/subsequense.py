def subsequense(sequense, target):
    """
    Return true if target is subsequense of sequense
    >>> subsequense("abcde","bcd")
    True
    >>> subsequense("abcde","bfd")
    False
    """

    if len(sequense) < len(target):
        return False
    
    temp = list(sequense)

    for i in target:
        if i in temp:
            del(temp[temp.index(i)])
        else:
            return False
    return True

def subsequense2(seq, target):
    """
    Return true if target is subsequense of sequense
    >>> subsequense2("abcde","bcd")
    True
    >>> subsequense2("abcde","bfd")
    False
    """
    if len(seq)<len(target):
        return False
    
    matches = []
    seq_list = list(seq)
    for i in target:
        try:
            matches.append(seq_list.pop(seq_list.index(i)))
        except:
            return False
    return len(target)==len(matches)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
