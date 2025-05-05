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
            # raise CancelledError

    try:
        await long_task
    except CancelledError:
        print('Our task was cancelled')


asyncio.run(main())

'''
Вызов cancel не прерывает задачу, делающую свое дело(когда задача исполняет Python-код);
он снимает ее, только если она уже находится в точке ожидания или
когда дойдет до следующей такой точки.
'''

'''
asyncio.create_task(delay(10)) adds the coroutine to the event loop, but it doesn’t start executing it immediately.
Real execution begins when the event loop gets a chance, for example, when main() hits await asyncio.sleep(1) and yields control.
'''
