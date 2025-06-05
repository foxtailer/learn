############# Decorators ##########
# import sys
# folder = '/home/zoy/git/learn/courses/Python Tutorial'
# if folder not in sys.path:
#     sys.path.append(folder)

# from decorators_pycon import CountCalls
###################################
    # outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():
        # declare nonlocal variable
        nonlocal message

        print("inner:", message)
        message = 'nonlocal'

    inner()
    print("outer:", message)

outer()