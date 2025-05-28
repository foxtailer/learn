############# Decorators ##########
# import sys
# folder = '/home/zoy/git/learn/courses/Python Tutorial'
# if folder not in sys.path:
#     sys.path.append(folder)

# from decorators_pycon import CountCalls
###################################

import inspect

frame = inspect.currentframe()
caller_frame = frame.f_back

print("Caller locals:")
print(caller_frame.f_locals)

print("Caller globals:")
print(caller_frame.f_globals)