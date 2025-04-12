import asyncio
from util import delay

async def add_one(number):
    return number + 1

async def hello_world():
    await delay(1) # 3 pause hello enter delay. 
    return "Hello World!" # 4 finish delay return from hello -> assign to message

async def main():
    message = await hello_world()  # 2 pause main run hello
    one_plus_one = await add_one(3)  # 5 pause main enter to plus -> assign
    print(one_plus_one) # 6
    print(message) # 7

asyncio.run(main()) # 1

"""
Создавая цикл событий, мы создаем пустую очередь задач. Затем
добавляем в эту очередь задачи для выполнения. На каждой ите-
рации цикла проверяется, есть ли в очереди готовая задача, и если
да, то она выполняется, пока не встретит операцию ввода-вывода.
В этот момент задача приостанавливается, и мы просим операцион-
ную систему наблюдать за ее сокетами. А сами тем временем пере-
ходим к следующей готовой задаче. На каждой итерации проверяет-
ся, завершилась ли какая-нибудь операция ввода-вывода; если да, то
ожидавшие ее завершения задачи пробуждаются и им предоставля-
ется возможность продолжить работу.
"""
