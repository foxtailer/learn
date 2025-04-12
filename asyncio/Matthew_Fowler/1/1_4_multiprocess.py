import multiprocessing
import threading
import time
import os


def hello_from_process():
    print(f'Привет от дочернего процесса {os.getpid()}/{threading.current_thread().name}!')


if __name__ == '__main__':
    hello_process = multiprocessing.Process(target=hello_from_process)
    hello_process.start()
    time.sleep(0.5)
    print(f'Привет от родительского процесса {os.getpid()}/{threading.current_thread().name}!')
    hello_process.join()
