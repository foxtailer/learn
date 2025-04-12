import time
import threading
import gevent
import multiprocessing


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    print(f'fib({number}) равно {fib(number)}')


def fibs_no_threading():
    print_fib(30)
    print_fib(31)


def fibs_with_threads():
    fortieth_thread = threading.Thread(target=print_fib, args=(30,))
    forty_first_thread = threading.Thread(target=print_fib, args=(31,))
    fortieth_thread.start()
    forty_first_thread.start()
    fortieth_thread.join()
    forty_first_thread.join()


def fibs_with_greenthreads():
    g1 = gevent.spawn(print_fib, 30)
    g2 = gevent.spawn(print_fib, 31)
    gevent.joinall([g1, g2])


def fibs_with_multiprocessint():
    p1 = multiprocessing.Process(target=print_fib, args=(30,))
    p2 = multiprocessing.Process(target=print_fib, args=(31,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


start = time.time()
fibs_no_threading()
end = time.time()
print(f'Время работы {end - start:.4f} с.')

print()

start_threads = time.time()
fibs_with_threads()
end_threads = time.time()
print(f'Многопоточное вычисление заняло {end_threads - start_threads:.4f} с.')

print()

start_threads = time.time()
fibs_with_multiprocessint()
end_threads = time.time()
print(f'Многопроцессорное вычисление заняло {end_threads - start_threads:.4f} с.')

print()

start_green = time.time()
fibs_with_greenthreads()
end_green = time.time()
print(f'Вычисление с зелёными потоками заняло {end_green - start_green:.4f} с.')
