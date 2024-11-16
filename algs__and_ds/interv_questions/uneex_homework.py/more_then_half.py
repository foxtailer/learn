'''
Имеется большая последовательность объектов (неважно каких), допускающих операцию сравнения. 
Известно, что некоторых одинаковых объектов в последовательности больше половины. Требуется,
 не храня последовательности, выяснить, чему они равны (т. е. вывести пример такого объекта). 
 Ввод построчный, последняя строка — пустая. Вывод делать с помощью обычного print().

Input:

int
int
float
int
str
str
int
str
int
int
float
int
int
float
int
float
Output:

<class 'int'>
'''

import sys

major_obj = None
count = 0

for cur_object in sys.stdin:
    cur_object = cur_object.strip()
    if not cur_object:
        break
    if count == 0:
        major_obj = cur_object
        count = 1
    elif major_obj == cur_object:
        count += 1
    else:
        count -= 1

print(eval(major_obj))