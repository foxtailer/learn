import os
import threading


print(os.name)

print(f'Исполняется Python-процесс с идентификатором: {os.getpid()}')
total_threads = threading.active_count()
thread_name = threading.current_thread().name
print(f'В данный момент Python исполняет {total_threads} поток(ов)')
print(f'Имя текущего потока {thread_name}')


# Вытесняюшая многозадачность - конкурентность в которой с помощью квантования
# времени задачам выделяется процессорное время и ОС управляет переключением 
# между ними
#
# Кооперативная многозадачность - точки переключиния между задачами определяются
# в коде программы

"""
Потоки можно представлять себе как облегченные процессы. Кроме
того, это наименьшая единица выполнения, которая может управ-
ляться операционной системой. У потоков нет своей памяти, они
пользуются памятью создавшего их процесса. Потоки ассоциирова-
ны с процессом, создавшим их. С каждым процессом всегда ассоци-
ирован по меньшей мере один поток, обычно называемый главным.
Процесс может создавать дополнительные потоки, которые обычно
называются рабочими или фоновыми.
"""