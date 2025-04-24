'''
если передать gather сопрограммы a и b именно в таком
порядке, то b может завершиться раньше, чем a. Но приятная особен-
ность gather заключается в том, что, независимо от порядка завер-
шения допускающих ожидание объектов, результаты гарантирован-
но будут возвращены в том порядке, в каком объекты передавались.
Продемонстрируем это в описанном ранее сценарии использования
функции delay.
'''

import sys
import asyncio

sys.path.append('/home/zoy/git/learn/asyncio/Matthew_Fowler/2')
from util import delay


async def main():
    results = await asyncio.gather(delay(3), delay(1))
    print(results)
    
asyncio.run(main())