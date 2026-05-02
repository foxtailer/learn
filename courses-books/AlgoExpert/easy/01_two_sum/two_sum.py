# Find out if in array are 2 numbers that in sum = target


# O(n) time | O(n) space
def two_sum(array, target):
    """
    >>> two_sum([1,6,3,5,8,-3],11)
    [6, 5]
    >>> two_sum([1,6,5,5,8,-3],10)
    [5, 5]
    >>> two_sum([1,6,2,5,8,-3],15)
    False
    """
    temp = set()

    for number in array:
        gift = target - number  # number + gift = target
        if gift in temp:
            return [gift, number]
        else:
            temp.add(number)

    return False
'''
# For indexes
def two_sum(array, target):
    seen = {}

    for i, num in enumerate(array):
        gift = target - num
        if gift in seen:
            return [seen[gift], i]
        seen[num] = i

    return None
'''


# O(nlog(n)) time | O(1) space
def two_sum2(array:list, target):
    """
    >>> two_sum2([1,6,3,5,9,-3],11)
    [5, 6]
    >>> two_sum2([1,6,2,5,8,-3],15)
    False
    """
    array.sort()
    L = 0  # Left start point
    R = len(array)-1  # Right start point

    while L<R:
        curent_sum = array[L] + array[R]
        
        if curent_sum < target:
            L += 1
        elif curent_sum > target:
            R -= 1
        else:
            return [array[L], array[R]]
            
    return False


# O(n^2) time | O(1) space
def two_sum3(array:list, target):
    """
    >>> two_sum3([1,6,3,4,8,-3],10)
    [6, 4]
    >>> two_sum3([1,11,2,4,-1,-3],10)
    [11, -1]
    >>> two_sum3([1,6,2,5,8,-3],15)
    False
    """ 
    start = 0
    for i in array:
        start += 1
        for j in array[start:]:
            if i + j == target:
                return [i, j]
    return False


def two_sum4(array, target):
    ...
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(two_sum([1,6,2,5,8,-3],10))
    print(two_sum2([1,6,2,5,8,-3],10))
    print(two_sum3([1,6,2,5,8,-3],10))
    print(two_sum4([1,6,2,5,8,-3],10))
