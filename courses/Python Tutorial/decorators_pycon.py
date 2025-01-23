import functools
from datetime import datetime
from inspect import signature
from unittest import result


# import time
# start = time.perf_counter()
# ...
# stop = time.perf_counter()
# {stop - start:.2f}


# import sys
# folder_path = "/path/to/your/folder"
# if folder_path not in sys.path:
#     sys.path.append(folder_path)

# import your_module


def timer(fu):
    @functools.wraps(fu)
    def wraper(*args, **kwargs):
        start_time = datetime.now()
        result = fu(*args, **kwargs)
        end_time = datetime.now()
        time_difference = (end_time - start_time).total_seconds()
        print(f'Execution time: {time_difference}s')
        return result
    return wraper


def trace(fu):
    name = fu.__name__  # Execute onse when we decorate fu

    @functools.wraps(fu)
    def _trace(*args, **kwargs): # Ewerithing inside executes each time we call function
        #print(f"Call {fu.__name__}{*args, kwargs}")
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()] # repr(v) = {v!r}
        signature = ', '.join(args_repr + kwargs_repr)
        print(f"Call {name}({signature})")
        result = fu(*args, **kwargs)
        print(f"{name} return {result!r}")
        return result
    return _trace


def count_calls(fu):

    @functools.wraps(fu)
    def _trace(*args, **kwargs):
        _trace.num_calls += 1
        result = fu(*args, **kwargs)
        return result
    
    _trace.num_calls = 0

    return _trace


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        return self.func(*args, **kwargs)


def supertrace(func=None, *, logger=print):

    def _supertrace_decorator(fu):
        name = fu.__name__  # Execute onse when we decorate fu

        @functools.wraps(fu)
        def _supertrace(*args, **kwargs): # Ewerithing inside executes each time we call function
            #print(f"Call {fu.__name__}{*args, kwargs}")
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()] # repr(v) = {v!r}
            signature = ', '.join(args_repr + kwargs_repr)
            logger(f"Call {name}({signature})")
            result = fu(*args, **kwargs)
            logger(f"{name} return {result!r}")
            return result
        return _supertrace
    
    if func is None:
        return _supertrace_decorator
    else:
        return _supertrace_decorator(func)
