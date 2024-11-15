"""
Ввести в столбик последовательность целых (положительных и отрицательных) чисел, не равных нулю; 
в конце этой последовательности стоит 0. Вывести наибольшую сумму последовательно идущих элементов 
этой последовательности (не менее одного).

2
3
-7
-1
3
4
5
-2
-4
7
8
-6
-1
0
Output:

21
"""

max_sum = float('-inf')
current_sum = 0

while True:
    number = int(input('number: '))
    if not number:
        break

    current_sum += number
    
    if current_sum > max_sum:
        max_sum = current_sum

    if current_sum < 0:
        current_sum = 0

print(max_sum)
