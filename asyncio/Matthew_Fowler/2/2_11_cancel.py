import asyncio
from asyncio import CancelledError
from util import delay


async def main():
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed = 0

    while not long_task.done():
        print('Task not finished, checking again in a second.')
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed == 5:
            long_task.cancel()

    try:
        await long_task  # canseled task can not be awaited again?
    except CancelledError:
        print('Our task was cancelled')


asyncio.run(main())

'''
Вызов cancel не прерывает задачу, делающую свое дело(когда задача исполняет Python-код);
он снимает ее, только если она уже находится в точке ожидания или
когда дойдет до следующей такой точки.
'''