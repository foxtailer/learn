import collections

def longest_subarray_langth(nums, k):
    n = len(nums)
    max_queue = collections.deque()
    min_queue = collections.deque()
    left = 0
    longest_len = 0

    for right in range(n):
        while max_queue and nums[right] > max_queue[-1]:
            max_queue.pop()
        while min_queue and nums[right] < min_queue[-1]:
            min_queue.pop()
        
        max_queue.append(nums[right])
        min_queue.append(nums[right])

        while max_queue[0] - min_queue[0] > k:
            if nums[left] == max_queue[0]:
                max_queue.popleft()
            if nums[left] == min_queue[0]:
                min_queue.popleft()
            left += 1

        longest_len = max(longest_len, right-left+1)
    
    return longest_len

print(longest_subarray_langth([1,2,3,2,7,9],2))
print(longest_subarray_langth([1,1,1,1,1],0))
