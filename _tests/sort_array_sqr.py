# [-5, 1, 2, 3]
# [1, 4, 9, 25]

array = [-5, 1, 2, 3]
print(sorted([x**2 for x in array]))

def sort_1(arr):
    start = 0
    for i in arr:
        if i < 0:
            start += 1
        else:
            temp = [x**2 for x in arr[start:]]
            break    
    for x in arr[start-1::-1]:
        temp.append(x**2) 
    return temp
print(sort_1(array))

 