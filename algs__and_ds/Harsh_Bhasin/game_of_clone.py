import random

def generate_list(l:int)->list:
    """Return a list of random numbers betwen 0 and l*2 with len - l"""
    result = []
    for i in range(l):
        result.append(random.randint(0, l*2))
    return result

def sort_game(a:list):
    last_unsorted_position = len(a)-1
    operation_count=0

    while last_unsorted_position > 0:
        for i in range(last_unsorted_position):
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
            operation_count+=1
        last_unsorted_position -= 1
    print('Finish', operation_count)

def sort_game_2(a:list):
    position_for_max = 0
    l = len(a)
    operation_count=0
    while position_for_max < l:
        max_item = a[position_for_max]
        for i in range(position_for_max, l):
            if a[i]>=max_item:
                max_item = a[i]
                max_item_index = i
            operation_count+=1
        a[position_for_max],a[max_item_index] = a[max_item_index],a[position_for_max]
        position_for_max+=1
    print('Finish', operation_count)
    


A = generate_list(100)
B = A[:]
sort_game_2(B)
sort_game(A)
print(A)
print(B)