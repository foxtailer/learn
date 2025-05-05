import asyncio
from util import delay

async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))

    await sleep_for_three
    # await sleep_again
    # await sleep_once_more
    # :)

asyncio.run(main())

'''
выполнение задач плани-
руется «как можно раньше». На практике это означает, что в точке,
где встречается первое после создания задачи предложение await, все
ожидающие задачи начинают выполняться, так как await запускает
очередную итерацию цикла событий.
'''

'''
код в задачах, не работает конкурентно с другими задачами; конкурентно 
задачи только спят.
'''