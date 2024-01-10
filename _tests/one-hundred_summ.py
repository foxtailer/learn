def one_hundred_summ(array):
    """
    >>> one_hundred_summ([20,30,70,80])
    True
    >>> one_hundred_summ([20,30,70,84])
    False
    >>> one_hundred_summ([20,30,34,70,84])
    False
    """
    left_index = 0
    right_index = len(array)-1

    while left_index < len(array)//2:
        if array[left_index] + array[right_index] != 100:
            return False
        
        left_index += 1
        right_index -= 1

    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()        