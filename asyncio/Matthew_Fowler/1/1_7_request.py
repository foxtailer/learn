import time
import requests
import threading


def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)


sync_start = time.time()
read_example()
read_example()
sync_end = time.time()
print(f'Синхронное выполнение заняло {sync_end - sync_start:.4f} с.')

print()

# request reliase gil when waiting for answer. becose it is i/o bound.
# Becose of it next tread can make request while first wait.
thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)

thread_start = time.time()
thread_1.start()
thread_2.start()
print('Все потоки работают!')
thread_1.join()
thread_2.join()
thread_end = time.time()
print(f'Многопоточное выполнение заняло {thread_end - thread_start:.4f} с.')


"""
Так почему же GIL освобождается при вводе-выводе, но не осво-
бождается для счетных задач? Все дело в системных вызовах, которые
выполняются за кулисами. В случае ввода-вывода низкоуровневые
системные вызовы работают за пределами среды выполнения Python.
Это позволяет освободить GIL, потому что код операционной систе-
мы не взаимодействует напрямую с объектами Python. GIL захваты-
вается снова, только когда полученные данные переносятся в объект
Python.
"""