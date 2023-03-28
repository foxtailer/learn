# Task 3
# sumator = make_sumator()
# sumator(1) -> 1
# sumator(2) -> 3
# sumator(3) -> 6

summ = 0

def make_sumator():
    def wrapper(x):
        global summ
        result = summ + x
        summ = result
        return result
    return wrapper

sumator = make_sumator()
print(sumator(1))
print(sumator(3))
print(sumator(2))

print("****")

def make_summator():
    value = 0
    def wrapper(x):
        nonlocal value
        value += x
        return value
    return wrapper

summator = make_summator()
print(summator(1))
print(summator(3))
print(summator(2))
