from asyncio import Future

my_future = Future()
print(f'my_future готов? {my_future.done()}')
my_future.set_result(42)
print(f'my_future готов? {my_future.done()}')
print(f'Какой результат хранится в my_future? {my_future.result()}')

'''
Если бы вместо
этого мы хотели записать во future исключение, то вызвали бы метод
set_exception.
ПРИМЕЧАНИЕ Мы не вызываем метод result, прежде чем ре-
зультат установлен, потому что тогда он возбудил бы исключе-
ние InvalidState.
'''