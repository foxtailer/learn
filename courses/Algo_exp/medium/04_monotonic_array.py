# O(n) time | O(1) space
def is_monotonic(array) -> bool:
    if len(array) <= 2:
        return True
    
    direction = array[1] - array[0]

    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i-1]
            continue
        if break_direction(direction, array[i-1], array[i]):
            return False

        return True


def break_direction(direction, previous_number, current_number):
    difference = current_number - previous_number

    if direction > 0:
        return difference < 0
    return difference > 0


def is_monotonic2(array):
    is_non_decreasing = True
    is_non_increasing = True

    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            is_non_decreasing = False
        if array[i] > array[i-1]:
            is_non_increasing = False

    return is_non_decreasing or is_non_increasing


print(is_monotonic([1,3,3,4]))
print(is_monotonic([1,3,2,4]))
print(is_monotonic([4,2,2,1]))
print(is_monotonic([4,2,3,1]))
print('@@@')
print(is_monotonic2([1,3,3,4]))
print(is_monotonic2([1,3,2,4]))
print(is_monotonic2([4,2,2,1]))
print(is_monotonic2([4,2,3,1]))