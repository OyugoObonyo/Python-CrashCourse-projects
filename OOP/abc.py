"""
Learning about abstract methods and classes
"""
from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod 
    def say_name(self, name):
        pass

class Bruno(Person):
    def say_name(self):
        print("Bruno's name is Bruno")
    
bruno = Bruno()
bruno.say_name()
