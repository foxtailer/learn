############# Decorators ##########
import sys
folder = '/home/zoy/git/learn/courses/Python Tutorial'
if folder not in sys.path:
    sys.path.append(folder)

from decorators_pycon import CountCalls
###################################


letters = ['z', 'A', 'a', 'Z']
letters.sort(key=str.lower)
#letters.sort(key=lambda x:x.lower())
print(letters)