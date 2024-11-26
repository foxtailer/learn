def longest_subarrray(self, nums, k):
    n = len(nums)
    max_queue = deque()
    min_qure = deque()
    left = 0
    longest_len = 0

    for right in range(n):
        #remove elements outside the current window from both queues
        