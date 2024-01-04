# [3,4,2,8,0,1,5], k=3
# [4,8,8,8,5]

array = [3,4,2,8,0,1,5]
WINDOW = 3
point = WINDOW -1
result = []

while point <= len(array)-1:
    print(array[point-(WINDOW-1):point+1])
    result.append(max(array[point-(WINDOW-1):point+1]))
    point += 1

print(result)

#TODO use dush data strukture