from collections import deque


def counter(n):
    while n > 0:
        yield n
        n -= 1

tasks = deque()
tasks.extend([counter(5), counter(10), counter(20)])

while tasks:
    task = tasks.popleft()
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task')
