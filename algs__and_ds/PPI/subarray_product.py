def check_subarray_product(nums, target):
    n = len(nums)
    left = 0
    product = 1

    for right in range(n):
        product *= nums[right]

        while product >= target and left <= right:
            if product == target:
                return True
            product //= nums[left]
            left += 1
    return False

def solo(nums, target):
    n = len(nums)
    left = 0
    product = 1

    for right in range(n):
        product *= nums[right]

        while product>=target and left<=right:
            if product == target:
                return True
            product//=nums[left]
            left +=1
    return False

# TODO use slise to acsept and move window, maby map to multiply objectsprint(check_subarray_product([1,2,3,4,5], 20))

print(check_subarray_product([1,2,3,4,5], 20))
print(solo([1,2,3,4,5], 20))