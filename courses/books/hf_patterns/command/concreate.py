from abstract import Command


class LightDevise():
    def on(self):
        print('Light on.')

    def off(self):
        print('Light off.')

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()


class SimpleRemoteControl:
    def set_command(self, command):
        self.command = command

    def button_was_pressed(self):
        self.command.execute()