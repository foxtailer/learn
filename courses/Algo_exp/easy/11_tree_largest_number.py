# Time O(n) | Space O(1)
def find_three_largest_number(array):
    three_largest = [None, None, None]
    for num in array:
        update_largest(three_largest, num)
    return three_largest


def update_largest(three_largest, num):
    if three_largest[2] is None or num > three_largest[2]:
        shift_and_update(three_largest, num, 2)
    elif three_largest[1] is None or num > three_largest[1]:
        shift_and_update(three_largest, num, 1)
    elif three_largest[0] is None or num > three_largest[0]:
        shift_and_update(three_largest, num, 0)
    

def shift_and_update(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i+1]


array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(find_three_largest_number(array))
