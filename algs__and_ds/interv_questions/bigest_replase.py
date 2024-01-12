def replase_right_big(arr):
    for i in range(len(arr)-1):
        arr[i]=max(arr[i+1:])
    arr[-1]=-1

a = [17,18,5,4,6,1]
replase_right_big(a)
print(a)