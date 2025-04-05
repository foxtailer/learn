from concreate import *


remote = SimpleRemoteControl()        # The invoker
light = LightDevise()                 # The receiver
light_on = LightOnCommand(light)      # The command

remote.set_command(light_on)          # Assign the command to the button
remote.button_was_pressed()           # Press the button
