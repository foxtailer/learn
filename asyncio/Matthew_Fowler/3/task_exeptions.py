import asyncio

async def boom():
    print("🔧 Задача boom начала работу")
    await asyncio.sleep(1)
    raise Exception("💥 Ошибка внутри задачи boom!")

# ✅ Способ 1: Ждать через await — исключение ловится нормально
async def handle_with_await():
    try:
        await boom()
    except Exception as e:
        print(f"[await] Поймали исключение: {e}")

# ✅ Способ 2: create_task + await
async def handle_with_task_and_await():
    task = asyncio.create_task(boom())
    try:
        await task
    except Exception as e:
        print(f"[task + await] Поймали исключение из task: {e}")

# ✅ Способ 3: create_task + .add_done_callback
def handle_exception_callback(task: asyncio.Task):
    if task.exception():
        print(f"[callback] Поймали исключение из callback: {task.exception()}")

async def handle_with_callback():
    task = asyncio.create_task(boom())
    task.add_done_callback(handle_exception_callback)
    await asyncio.sleep(2)  # ждем завершения задачи

# ❌ Способ 4: Запускаем create_task и НИЧЕГО не делаем
async def fire_and_forget(): 
    asyncio.create_task(boom())
    await asyncio.sleep(2)  # ждем, но не ловим исключение

# 👇 Главная функция запускает каждый случай по очереди
async def main():
    print("\n--- 1. await ---")
    await handle_with_await()

    print("\n--- 2. task + await ---")
    await handle_with_task_and_await()

    print("\n--- 3. task + callback ---")
    await handle_with_callback()

    print("\n--- 4. create_task (НЕ ЛОВИМ!) ---")
    await fire_and_forget()  # Тут увидим WARNING

asyncio.run(main())
