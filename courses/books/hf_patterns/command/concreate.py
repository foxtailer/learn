from abstract import Command


class NoCommand(Command):
    def execute(self):
        print("No command assigned.")
    def undo(self):
        print("No command assigned.")


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
    
    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class GarageDoor:
    def up(self):
        print("Garage door is OPENING...")

    def down(self):
        print("Garage door is CLOSING...")

    def stop(self):
        print("Garage door is STOPPED.")

    def light_on(self):
        print("Garage light is ON.")

    def light_off(self):
        print("Garage light is OFF.")


class GarageDoorOpenCommand(Command):
    @staticmethod
    def swap():
            while True:
                yield 0
                yield 1

    def __init__(self, garage_door):
        self.garage_door = garage_door
        self._swap = self.swap()

    def execute(self):
        self.garage_door.up()
   
    def undo(self):
        if not next(self._swap):
            self.garage_door.down()
        else:
            self.garage_door.up()

class GarageDoorCloseCommand(Command):
    @staticmethod
    def swap():
            while True:
                yield 0
                yield 1

    def __init__(self, garage_door):
        self.garage_door = garage_door
        self._swap = self.swap()

    def execute(self):
        self.garage_door.down()

    def undo(self):
        if not next(self._swap):
            self.garage_door.up()
        else:
            self.garage_door.down()


class RemoteControl:
    def __init__(self):
        self.on_commands = [NoCommand() for _ in range(7)]
        self.off_commands = [NoCommand() for _ in range(7)]
        self.undo_command = NoCommand()

    def set_command(self, slot, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def off_button_was_pushed(self, slot):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def undo_button_was_pushed(self):
        self.undo_command.undo()
    
    # For lambda test
    def on_button_was_pushed_2(self, slot):
        self.on_commands[slot]()
    # For lambda test
    def off_button_was_pushed_2(self, slot):
        self.off_commands[slot]()

    def __str__(self):
        output = ["\n------ Remote Control -------"]
        for i, (on_cmd, off_cmd) in enumerate(zip(self.on_commands, self.off_commands)):
            output.append(f"[slot {i}] {on_cmd.__class__.__name__}    {off_cmd.__class__.__name__}")
        return "\n".join(output)