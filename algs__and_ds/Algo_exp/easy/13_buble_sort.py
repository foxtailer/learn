# O(n^2) time | O(1) space
def buble_sort(array):
    is_sorted = False
    step = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(array)-(1+step)):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                is_sorted = False
        step += 1
    return array


array = [5, 2, 8, 5, 6, 3, 9]
print(buble_sort(array))
