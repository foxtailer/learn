import random
import functools


def decorator(param='decorator'):
    def wraper(fu):
        @functools.wraps(fu)
        def _wraper(*args, **kwargs):
            print(f'Before fu.({param})')
            result = fu(*args, **kwargs)
            print(f'After fu.({param})')
            return result
        return _wraper
    return wraper


@decorator()
def dise_roll(n):
    return random.randint(1, n)


print(dise_roll(6))
print(dise_roll(6))
print(dise_roll.__name__)