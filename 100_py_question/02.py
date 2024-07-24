# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

#01
x = int(input("Factorial of: "))
result = 1

for i in range(2, x+1):
    result *= i

print("01: ",result)

#02
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print('02', factorial(x))

#03
result = 1
while x:
    result *= x
    x -= 1
print('03', result)