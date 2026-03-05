# O(n^2) time | O(1) space
def selection_sort(array):
    current_index = 0
    while current_index < len(array)-1:
        smallest_index = current_index

        for i in range(current_index, len(array)):
            if array[smallest_index] > array[i]:
                smallest_index = i
    
        array[current_index], array[smallest_index] = array[smallest_index], array[current_index]
        current_index += 1

    return array

array = [8,5,2,9,5,6,3]
print(selection_sort(array))
