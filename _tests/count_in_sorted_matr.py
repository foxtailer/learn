sm_list =[
[0,0,0,0,0,1],
[0,0,0,0,1,1],
[0,0,0,1,1,1],
[0,0,0,1,1,1],
[0,1,1,1,1,1],
[1,1,1,1,1,1],
]

def count(li:list):
    x=len(li[0])-1
    y=0
    sum=0

    while y < len(li)-1 and x >= 0:
        if li[y][x] == 0:
            sum += x+1
            y+=1
        else:
            x-=1
    
    return sum

print(count(sm_list))