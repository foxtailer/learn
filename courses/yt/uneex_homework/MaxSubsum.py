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
Последовательность с наибольшей суммой — от второй тройки до восьмёрки.


21
Подсказка: элементы вводятся в столбик, потому что в эффективном алгоритме их вообще не надо хранить.
"""

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
