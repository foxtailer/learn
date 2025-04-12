import asyncio
from util import delay

async def main():
    # create task from courutine
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    result = await sleep_for_three
    print(result)
    print('@')

    # await sleep_for_three
    # print('@')


asyncio.run(main())

'''
Задача – это обертка вокруг сопрограммы, которая планирует выполнение 
последней в цикле событий. И планирование, и выполнение происходят в неблокирующем режиме
'''

"""
Для создания задачи служит функция asyncio.create_task. Ей переда-
ется подлежащая выполнению сопрограмма, а в ответ она немедлен-
но возвращает объект задачи. Этот объект можно включить в выраже-
ние await, которое извлечет возвращенное значение по завершении
задачи.
"""

"""
В asyncio цикл событий управляет очередью задач.
Задача – это обертка(async function) вокруг сопрограммы. Сопрограмма(code in async function)
может приостановить выполнение(await), встретив операцию ввода-вывода, и дать циклу
событий возможность выполнить другие задачи, которые не ждут завершения ввода-вывода.
*сопрограмма(corщutine in cooperate multitask concurensy)
"""