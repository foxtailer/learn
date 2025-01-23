############# Decorators ##########
import sys
folder = '/home/zoy/vscode/learn/courses/Python Tutorial'
if folder not in sys.path:
    sys.path.append(folder)

from decorators_pycon import CountCalls
###################################


@CountCalls
def fibo(number):
    if number < 2:
        return 1
    
    return fibo(number -1) + fibo(number - 2)


print(fibo(7))
print(fibo.num_calls)