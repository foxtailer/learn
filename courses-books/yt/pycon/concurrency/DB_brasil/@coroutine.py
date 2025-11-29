from types import coroutine


@coroutine
def spam():
    result = yield 'somevalue'
    print('The result is', result)


# f = spam()
# print('\n\n')
# print(f.send(None))  # somevalue
# print(f.send(42))  # The result is 42. StopIteration


async def foo():
    print('Start foo')
    await spam()
    print('End foo')


f = foo()
print('\n\n')
f.send(None)  # Start foo
f.send(42)  # The result is 42. StopIteration
