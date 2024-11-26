def find_sum_of_nearest_ge(nums:list):
    n = len(nums)
    stack = []
    left_greaters = [-1]*n
    right_greaters = [-1]*n
    sum_greater = 0

    # Calculate the nearest greater elenents on the legt side
    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            left_greaters[i] = nums[stack[-1]]
        stack.append(i)

    # Clear the stack and calculate the nearest greater elenemts on the right side
    stack.clear()
    for i in range(n -1, -1, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            right_greaters[i] = nums[stack[-1]]
        stack.append(i)
    
    # Calculate the sum of the rearest greater elenemts for each element
    for i in range(n):
        sum_greater += left_greaters[i] + right_greaters[i]
    
    return sum_greater


def find_nearest_max(nums:list):
    index = 0
    result_sum = 0
    n = len(nums)

    if index == 0:
        result_sum += (-1)+max(nums[1:])
    elif index == n - 1:
        result_sum += max(nums[:-1])+(-1)
    
    

print(find_sum_of_nearest_ge([3,6,8,2,7,5]))
