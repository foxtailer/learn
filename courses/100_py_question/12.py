# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that 
# each digit of the number is an even number.The numbers obtained should be printed in a 
# comma-separated sequence on a single line.

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

result = []
for i in range(1000, 3001):
    flag = True
    for j in str(i):
        if int(j) % 2 != 0:
            flag = False
    if flag:
        result.append(i)

print(result)

def check(element):
    return all(ord(i)%2 == 0 for i in element)  # all returns True if all digits i is even in element

lst = [str(i) for i in range(1000,3001)]        # creates list of all given numbers with string data type
lst = list(filter(check,lst))                   # filter removes element from list if check condition fails
print(",".join(lst))
