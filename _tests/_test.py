############# Decorators ##########
# import sys
# folder = '/home/zoy/git/learn/courses/Python Tutorial'
# if folder not in sys.path:
#     sys.path.append(folder)

# from decorators_pycon import CountCalls
###################################

'__hash__' in dir(list())  # True
list().__hash__ is None  # True

class HashList(list):
    def __hash__(self):
        return 1
    
    def __eq__(self, value):
        return True
    
hl1 = HashList((1,2))
hl2 = HashList((3,4))
hl1.__eq__(hl2)  # False

d = {hl1: 'one', hl2: 'two'}
print(d)