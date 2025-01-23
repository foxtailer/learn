def hello(cls):
    original_init = cls.__init__
    def _hello_init(*args, **kwargs):
        print(f'An instance of {cls.__name__} was created')
        return original_init(*args, **kwargs)
    cls.__init__ = _hello_init
    return cls

@hello
class Thing:
    ...

thing = Thing()

print(isinstance(thing, Thing))
