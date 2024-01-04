def find_sum_of_nearest_ge(nums):
    n = len(nums)
    stack = []
    left_greaters = [-1]*n
    right_greaters = [-1]*n
    sum_greater = 0

    # Calculate the mearest greater elenents on the legt side
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