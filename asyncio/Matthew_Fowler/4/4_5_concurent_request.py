import asyncio

sys.path.append('/home/zoy/git/learn/asyncio/Matthew_Fowler/2')
from util import async_timed, delay


@async_timed()
async def main() -> None:
    # When we have many tasks we want to create them in loop
    # Здесь имеется тонкая ошибка. Все дело в том, что мы применяем
    # await сразу же после создания задачи. Это значит, что мы приостанав-
    # ливаем списковое включение и сопрограмму main для каждой создан-
    # ной задачи delay до момента, когда она завершится. В данном случае
    # в каждый момент времени будет работать только одна задача, а не все
    # конкурентно.
    delay_times = [3, 3, 3]
    [await asyncio.create_task(delay(seconds)) for seconds in delay_times]


@async_timed()
async def main() -> None:
    # This will work but
    # Если в какой-то сопрограмме возникает исклю-
    # чение, то оно будет возбуждено в момент ожидания сбойной задачи.
    # Это значит, что мы не сможем обработать успешно завершившиеся
    # задачи, потому что одно-единственное исключение останавливает
    # всю работу.
    delay_times = [3, 3, 3]
    tasks = [asyncio.create_task(delay(seconds)) for seconds in delay_times]
    [await task for task in tasks]


asyncio.run(main())