"""
Для создания и приостановки сопрограммы нам придется исполь-
зовать ключевые слова Python async и await. Слово async определяет
сопрограмму, а слово await приостанавливает ее на время выполне-
ния длительной операции.
"""

import asyncio


# create courutine
async def add_one(num: int)->int:
    return num+1

# main are paused when call await (it fase i/o operation(fake))
# after add_one finish, main wake up
async def main():
    step_one = await add_one(1)   # call corutine - pause main
    step_too = await add_one(step_one) # up main - call corutine - pause again
    # if i/o bount we send it to os until it done

    print(step_one)
    print(step_too)


# Start main loop with task main
asyncio.run(main())

"""
asyncio.run – то, что она задумана
как главная точка входа в созданное нами приложение asyncio. Она
выполняет только одну сопрограмму, и эта сопрограмма должна по-
заботиться обо всех остальных аспектах приложения. Далее мы будем
использовать эту функцию почти во всех наших приложениях. Сопро-
грамма, которую выполняет asyncio.run, должна создать и запустить
все прочие сопрограммы
"""

'''
 3a await обычно следует обращение к сопрограмме (точнее, к объекту, допу-
скающему ожидание, который необязательно является сопрограммой)
'''
