# O(nlon(n) + mlog(m)) time | O(1) space
def smallest_difference(array_1, array_2):
    array_1.sort()
    array_2.sort()

    idx_1, idx_2 = 0, 0

    smallest = float('inf')
    current = float('inf')
    smallest_pair =[]

    while idx_1 < len(array_1) and idx_2 < len(array_2):
        first_num = array_1[idx_1]
        second_num = array_2[idx_2]

        if first_num < second_num:
            current = second_num - first_num
            idx_1 += 1
        elif second_num < first_num:
            current = first_num - second_num
            idx_2 += 1
        else:
            return [first_num, second_num]

        if smallest > current:
            smallest = current
            smallest_pair = [first_num, second_num]
        
    return smallest_pair


a = [-1, 5, 10, 20, 28, 3]
b = [26, 134, 135, 15, 17]

print(smallest_difference(a, b))
