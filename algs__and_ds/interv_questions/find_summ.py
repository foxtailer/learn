def find_summ(nums, target):
    nums.sort()
    left = 0
    right = len(nums)-1
    while left<=right:
        if nums[left]+nums[right] > target:
            right-=1
        elif nums[left]+nums[right] < target:
            left+=1
        elif nums[left]+nums[right] == target:
            return (nums[left], nums[right])

print(find_summ([1,3,4,5,7,5], 9))