
def two_sum(array, target):
    """
    >>> two_sum([1,6,2,5,8,-3],11)
    [3, 1]
    >>> two_sum([1,6,2,5,8,-3],15)
    False
    """
    temp = {}

    for i in range(len(array)):
        gift = target - array[i]
        if gift in temp:
            return [i, temp[gift]]
        else:
            temp[array[i]] = i

    return False

def two_sum2(array:list, target):
    """
    >>> two_sum([1,6,2,5,8,-3],11)
    [3, 1]
    >>> two_sum([1,6,2,5,8,-3],15)
    False
    """
    array.sort()
    L = 0
    R = len(array)-1

    while L<R:
        curent_sum = array[L]+array[R]
        if curent_sum < target:
            L += 1
        elif curent_sum > target:
            R -= 1
        else:
            return [L, R]
    
    return False



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(two_sum2([1,6,2,5,8,-3],10))
    print(two_sum([1,6,2,5,8,-3],10))