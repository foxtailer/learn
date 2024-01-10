def intersection(arr_1, arr_2):
    flag = 0
    result = []
    if arr_1 > arr_2:
        temp = {i:True for i in arr_1}
        flag = 1
    else:
        temp = {i:True for i in arr_2}
        flag = 2
    if flag == 1:
        for item in arr_2:
            try:
                if temp[item]==True:
                    result.append(item)
            except:
                continue            
    if flag == 2:
        for item in arr_1:
            try:
                if temp[item]==True:
                    result.append(item)
            except:
                continue
    return result

print(intersection([1,3,4,5,6,9], [2,3,5,9,12]))