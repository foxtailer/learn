max_subsum = float('-inf')
current_sum = 0

1
while n := int(input(': ')):

    current_sum = max(n, current_sum + n)
    max_subsum = max(max_subsum, current_sum)


# 2
# while number := int(input()):
#     current_sum += number
#     if current_sum < 0:
#         current_sum = 0
#     if current_sum > max_subsum:
#         max_subsum = current_sum


print(max_subsum)
