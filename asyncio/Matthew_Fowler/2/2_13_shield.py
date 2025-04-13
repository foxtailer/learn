import asyncio
from util import delay


async def main():
    task = asyncio.create_task(delay(10))
    try:
        # asyncio.shield функция предотвращает снятие сопрограммы, 
        # снабжая ее «щитом», позволяющим игнорировать запросы на снятие.
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except TimeoutError:
        print("Задача заняла более 5 с, скоро она закончится!")
        await delay(3)
        result = await task  # The coroutine pauses, yielding control to the event loop.
        print(result)


asyncio.run(main())

'''
await asyncio.wait_for(delay(2), timeout=1)
You are passing a coroutine, not a task.
So what does wait_for() do with that coroutine?

🔍 Under the hood
asyncio.wait_for() sees you're passing a coroutine, so it automatically wraps it into a Task:

inner_task = asyncio.create_task(delay(2))
That task is internal to wait_for() — you didn’t create it yourself, so you don’t have a reference 
to it. That’s why we call it an inner task — it's a hidden, temporary task that wait_for() controls.

So when a timeout happens, wait_for() cancels that internal task — but you can’t check its status, 
because you don’t have access to it.
'''