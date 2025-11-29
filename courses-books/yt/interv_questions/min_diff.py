def min_dif(arr):
    sort_arr = sorted(arr)
    size = len(sort_arr)
    _min_dif = 9999*999

    for i in range(size-1):
        dif = sort_arr[i+1] - sort_arr[i]
        if dif < _min_dif:
            _min_dif = dif
        return _min_dif

arr = [5, 32,45,4,12,18,25] 
print(min_dif(arr))
