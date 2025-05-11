############# Decorators ##########
import sys
folder = '/home/zoy/git/learn/courses/Python Tutorial'
if folder not in sys.path:
    sys.path.append(folder)

from decorators_pycon import CountCalls
###################################


x = 100

for i in range(x):
    print(i)
