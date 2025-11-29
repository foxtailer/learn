# The Command pattern encapsulates a request as an object, allowing for the 
# parameterization of client objects with different requests, the organization 
# of a queue or logging of requests, and the support for undoing operations.

'''
Паттерн Команда отделяет сторону, выдающую запрос, от объекта,
фактически выполняющего операцию. В нашем примере запрос поступает
от пульта, а объектом, выполняющим операцию, будет экземпляр одного из
классов устройств.

Для этого в архитектуру приложения вводятся объекты команд. Сам пульт 
понятия не имеет, что это за операция, — он знает только,
как взаимодействовать с нужным объектом для выполнения операции.(командой)
'''

'''
Client(CreateOrder) -> Waiter(TakeOrder) -> Waiter(OrderUp) ->
Chefe(ReadInstructionsFromOrder)

Бланк заказа инкапсулирует запрос на приготовление блюд.
Заказ содержит ссылку на объект, который должен
готовить блюда (Short-Order Cook). Инкапсуляция заключа-
ется в том, что Официантку не интересует содержимое за-
каза и то, кто будет его выполнять; она только кладет заказ
на стойку и сообщает: «Поступил заказ!»

В течение рабочего дня метод takeOrder() класса Офици-
антки вызывается с множеством разных заказов от разных
посетителей, но это Официантку не смущает. Она знает,
что все Заказы поддерживают метод orderUp()
'''

from concreate import *


remote = RemoteControl()
light = LightDevise()
garage = GarageDoor()

light_on = LightOnCommand(light)
light_off = LightOffCommand(light)
garage_open = GarageDoorOpenCommand(garage)
garage_close = GarageDoorCloseCommand(garage)

remote.set_command(0, light_on, light_off)
remote.on_button_was_pushed(0)
remote.off_button_was_pushed(0)

remote.set_command(1, garage_open, garage_close)
remote.on_button_was_pushed(1)
remote.off_button_was_pushed(1)
remote.undo_button_was_pushed()
remote.undo_button_was_pushed()
remote.undo_button_was_pushed()

# Use lambda instead of Command class 
remote.set_command(2, lambda: light.on(), lambda: light.off())
remote.on_button_was_pushed_2(2)
remote.off_button_was_pushed_2(2)

print()
print(remote)
