import random

M = [(1,3), (3,5), (1,1), (3,6), (7,2), (5,4), (1,1), (2,2)]
bag_size = 5
max_value = 2**len(M)

all_value = []

while len(all_value)<max_value:
    random.shuffle(M)
    temp = M[:3]
    if temp not in all_value:
        all_value.append(temp)

top_set_worth = 0
for set_ in all_value:
    sum_of_weight = 0
    sum_of_worth = 0
    for weight, worth in set_:
        sum_of_weight += weight
        sum_of_worth += worth
    if sum_of_weight <= bag_size and sum_of_worth>top_set_worth:
        print(set_)