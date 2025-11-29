# Queue (FIFO - First In, First Out)

from collections import deque

queue = deque([1, 2, 3])  # queue -> [1, 2, 3].


queue.append(4)  # queue -> [1, 2, 3, 4]. O(1)
queue.popleft()  # return 1, queue -> [2, 3, 4]. O(1)
queue[0]  # return 1. O(1)
len(queue) == 0  # return False. O(1)
queue.reverse()  # queue reversed. O(n)
queue.copy()  # return deque([1, 2, 3]). O(n)
queue.clear()  # queue -> []. O(n)
