
"""Use only if we cnow all possible characters"""
N = 10

F = [0] * 10  # 10 - possible characters 0 to 9

for i in range(N):
    x = int(input("Enter number: "))
    F[x] += 1


result = []
for i in range(len(F)):
    for j in range(F[i]):
        result.append(i)

print(result)