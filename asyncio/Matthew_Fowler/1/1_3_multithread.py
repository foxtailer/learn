import threading
import time


def hello_from_thread():
    print(f'Привет от потока {threading.current_thread()}!')


hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

time.sleep(0.5)  # Becose of delay hello_thread finished first.

print(f'В данный момент Python выполняет {total_threads} поток(ов)')
print(f'Имя текущего потока {thread_name}')

hello_thread.join()  # Guarantees the hello_thread finishes
