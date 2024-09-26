# O(n) time | O(1) space
def move_element_to_end(array, to_move):
    i = 0
    j = len(array) - 1

    while i < j:
        while i < j and array[j] == to_move:
            j -= 1
        
        if array[i] == to_move:
            array[i], array[j] = array[j], array[i]
        i += 1

    return array


def move_element_to_end2(array, to_move):
    i = 0
    j = len(array)-1

    while i < j:
        if array[j] == to_move:
            j -= 1
            continue

        if array[i] == to_move:
            array[i], array[j] = array[j], array[i]
        i += 1

    return array


array = [2,1,2,2,2,3,4,2]

print(move_element_to_end(array, 2))
print(move_element_to_end2(array, 2))
