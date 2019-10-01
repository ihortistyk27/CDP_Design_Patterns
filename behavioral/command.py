
from abc import ABCMeta, abstractstaticmethod


# Receiver
class Light:

    def switch_on(self):
        print("The light is ON")

    def switch_off(self):
        print("The light is OFF")


# ICommand Interface
class ICommand(metaclass=ABCMeta):
    @abstractstaticmethod
    def execute(self):
        pass


# Command ON
class SwitchOnCommand(ICommand):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.switch_on()


# Command OFF
class SwitchOffCommand(ICommand):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.switch_off()


# Invoker
class Switch:
    """Invoker class"""

    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands:
            self._commands[command_name].execute()
        else:
            print("Could not find the command")


# Client
if __name__ == "__main__":
    LIGHT = Light()

    # Commands
    SWITCH_ON = SwitchOnCommand(LIGHT)
    SWITCH_OFF = SwitchOffCommand(LIGHT)

    # Invoker
    SWITCH = Switch()

    # Register command in the invoker
    SWITCH.register("ON", SWITCH_ON)
    SWITCH.register("OFF", SWITCH_OFF)

    SWITCH.execute("ON")
    SWITCH.execute("OFF")
