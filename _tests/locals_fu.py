def fu(*arg, **kwarg):
    print(locals())

fu(1,2,3,4, b=2,c=4,t=5)
