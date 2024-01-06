def bin_search(arr, target):
    start_index = 0
    end_index = len(arr)-1
    step = 0

    while start_index <= end_index:
        mid_point = (end_index+start_index)//2
        mid_item = arr[mid_point]
        step += 1
        
        if mid_item == target:
            print(step)
            return mid_point
        elif mid_item < target:
            start_index = mid_point+1
        elif mid_item > target:
            end_index = mid_point-1
        else:
            print(step)
            return None
    
print(bin_search(list(range(100)), 35))


