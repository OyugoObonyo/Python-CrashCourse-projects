"""
High-level modules should not depend on the low-level modules.
Both should depend on abstractions.
Abstractions should not depend on details. Details should depend on abstractions.
Only possible when you separate creation from use
Instead of directly coupling two classes by calling a class in another class or method, 
call an abstraction of said class
"""
from abc import ABC, abstractmethod

# Example1 without dependency inversion implementation

class LightBulb:
    def turn_on(self):
        print("Lightbulb is turned on ...")

    def turn_off(self):
        print("LIghtbulb is turned off ...")


class ElectricPowerSwitch:
    def __init__(self, l: LightBulb):
        self.lightBulb = l
        self.on = False

    def press(self):
        if self.on:
            self.lightBulb.turn_off()
            self.on = False
        else:
            self.lightBulb.turn_on()
            self.on = True

l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()

# Example1 with dependency inversion implementation
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("Lightbulb is turned on ...")

    def turn_off(self):
        print("LIghtbulb is turned off ...")

class TelevisionSet(Switchable):
    def turn_on(self):
        print("TV Set is turned on ...")

    def turn_off(self):
        print("TV Set is turned off ...")


class ElectricPowerSwitch:
    def __init__(self, switchable: Switchable):
        self.switchable = switchable
        self.on = False

    def press(self):
        if self.on:
            self.switchable.turn_off()
            self.on = False
        else:
            self.switchable.turn_on()
            self.on = True



l = LightBulb()
tv = TelevisionSet()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()
tv_switch = ElectricPowerSwitch(tv)
tv_switch.press()
tv_switch.press()  