numbers = [1,3,4,5]

def lost_num(numbers:list)->int:
    return int(((numbers[-1]*(numbers[-1]+1))/2)-sum(numbers))

def lost_num_2(numbers):
    xor_a = numbers[0]
    xor_b = 0
    max_item = numbers[-1]
    for i in range(1,max_item-1):
        xor_a = xor_a^numbers[i]
    for i in range(1, max_item+1):
        xor_b ^= i
    return xor_a^xor_b

print(lost_num(numbers))
print(lost_num_2(numbers))