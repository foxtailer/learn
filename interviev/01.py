def my_range(start, stop=None):
    start, stop = fu(start, stop)

    if stop == 0:
        return

    while True:
        yield start
        start += 1
        if start > stop-1:
            return


def fu(start, stop):
    if start and stop is not None:
        return (start, stop)
    else:
        return(0, start)

# print(list(range(10))) # start = 0, stop = 10
# print(list(my_range(10)))

# print(list(range(0)))  
# print(list(my_range(0)))

# print(list(range(5, 15))) 
# print(list(my_range(5, 15)))

print(list(range(-10, 0))) 
print(list(my_range(-10, 0)))
