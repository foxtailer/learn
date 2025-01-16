import functools
from datetime import datetime
from inspect import signature


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
