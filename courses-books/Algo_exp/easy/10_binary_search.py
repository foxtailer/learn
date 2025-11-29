# Return index of item in sorted list

# Time O(log(n))
# Space O(1) | O(log(n))-for recursion
def binary_search(array, target):
    return bs_helper(array, target, 0, len(array)-1)

def bs_helper(array, target, left, right):
    if left > right:
        return
    
    middle = (left + right) // 2
    potential_match = array[middle]
    
    if target == potential_match:
        return middle
    elif target < potential_match:
        return bs_helper(array, target, left, middle-1)
    else:
        return bs_helper(array, target, middle+1, right)


# O(log(n)) time | O(1) space
def binary_search2(array, target):
    left = 0
    right = len(array)-1

    while left <= right:
        middle = (left + right) // 2
        potential_match = array[middle]
        
        if target == potential_match:
            return middle
        elif target < potential_match:
            right = middle-1
        else:
            left = middle+1
    return

arr = [0,1,21,33,45,45,61,71,72,73]
print(binary_search(arr, 33), 
      binary_search2(arr, 33))
