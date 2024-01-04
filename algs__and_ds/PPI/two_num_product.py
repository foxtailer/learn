"""
given:
array:list of int
target:int
goal:
find 2 number whose product = target
"""

def tnp(arr:list, targer:int):
    point = 1
    for i in arr:
        for j in arr[point:]:
            if i*j == targer:
                return [arr.index(i), arr.index(j)]
        point += 1


def two_number_prpduct(nums, target):
    num_index_map = {}

    for index, num in enumerate(nums):
        if num == 0 and target == 0:
            if num.count(0) > 1:
                return [index for index, n in enumerate(nums) if n == 0][:2]
        if target%num == 0:
            complement = target//num
            if complement in num_index_map:
                return [num_index_map[complement], index]
        num_index_map[num] = index

def tnp_solo(nums:list, target:int):
    num_map = {}
    for index, num in enumerate(nums):
        if num == 0 and target == 0:
            if nums.count(0) > 1:
                return [index for index, n in enumerate(nums) if n == 0][:2]
        if target%num == 0:
            complement = target//num
            if complement in num_map:
                return [index, num_map[complement]]
        num_map[num] = index



print(tnp([1,2,4,6,8], 12)) # >>> [1,3]
print(tnp_solo([1,2,4,6,8], 12)) # >>> [1,3]
print(two_number_prpduct([1,2,4,6,8], 12)) # >>> [1,3]

print(tnp([1,4,6,8,0], 0)) # >>> [0,4]
print(tnp([1,4,0,6,8], 0)) # >>> [0,4]