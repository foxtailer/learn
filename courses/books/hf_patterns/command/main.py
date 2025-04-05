# The Command pattern encapsulates a request as an object, allowing for the 
# parameterization of client objects with different requests, the organization 
# of a queue or logging of requests, and the support for undoing operations.

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

# Use lambda instead of Command class 
remote.set_command(2, lambda: light.on(), lambda: light.off())
remote.on_button_was_pushed_2(2)
remote.off_button_was_pushed_2(2)

print()
print(remote)
