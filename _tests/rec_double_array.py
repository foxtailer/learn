def double_array(arr, index=0):
    if (index >= len(arr)):
        return
    arr[index] *= 2
    double_array(arr, index+1)

array = [1,2,3]
double_array(array)
print(array)
