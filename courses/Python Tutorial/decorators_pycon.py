import functools
from datetime import datetime

# import time
# start = time.perf_counter()
# ...
# stop = time.perf_counter()
# {stop - start:.2f}


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