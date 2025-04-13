import asyncio
from util import delay


async def main():
    delay_task = asyncio.create_task(delay(2))

    try:
        # wait_for принимает объект сопрограммы или задачи и тайм-аут в секун
        # дах и возвращает сопрограмму, к которой можно применить await.
        # Если задача не завершилась в отведенное время, то возбуждается ис-
        # ключение TimeoutError и задача автоматически снимается.
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут!')
        print(f'Задача была снята? {delay_task.cancelled()}')


asyncio.run(main())