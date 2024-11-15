"""
Ввести по одному в строке целые числа, не равные нулю (не менее одного, конец ввода — 0), вывести 
второй максимум последовательности (число, строго меньшее максимума последовательности, и не меньшее 
остальных чисел в ней), и NO, если такового нет.

Input:

1
2
3
4
3
2
1
0
Output:

3
"""
top = 0
prev_top = 0

while True:
    number = int(input('number: '))
    if not number:
        break

    if number > top:
        prev_top = top
        top = number
        continue
    
    if number > prev_top:
        prev_top = number

print(prev_top)
