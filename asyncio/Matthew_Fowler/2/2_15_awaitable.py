from asyncio import Future
import asyncio


def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))  # Task that set future value
    return future

async def set_future_value(future) -> None:
    await asyncio.sleep(1)  # Wait 1s before set
    future.set_result(42)

async def main():
    future = make_request()
    print(f'Будущий объект готов? {future.done()}')
    value = await future  # pause main before set value
    print(f'Будущий объект готов? {future.done()}')
    print(value)

asyncio.run(main())

'''
task напрямую наследует future. Можно считать, что объ-
ект future представляет значение, которое появится только в буду-
щем. А task является комбинацией сопрограммы и future. Создавая
задачу, мы создаем пустой объект future и запускаем сопрограмму.
А когда сопрограмма завершится с результатом или вследствие ис-
ключения, мы записываем этот результат или объект-исключение во
future.
'''

'''
            Awaitable
            ____|____
           |         |
       Coroutine   Future
                      |
                    Task   
'''
