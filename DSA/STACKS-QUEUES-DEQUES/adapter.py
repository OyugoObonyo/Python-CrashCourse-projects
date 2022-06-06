"""
Trying out the adapter design pattern
"""

from abc import ABC, abstractmethod

class AbstractClassA(ABC):
    @abstractmethod
    def methodA(self):
        pass

class ImplementationA(AbstractClassA):
    @abstractmethod
    def methodA(self):
        print("This is method A")

class AbstractClassB(ABC):
    @abstractmethod
    def methodB(self):
        pass

class ImplementationB(AbstractClassB):
    def methodB(self):
        print("This is method B")

# Now create an adapter for class B which implements the interface of class A
class ImplementationBAdapter(AbstractClassA):
    def __init__(self) -> None:
        # make an instancr of the adapted class a private attribute
        self._classB = ImplementationB()
        

    def methodA(self):
        self._classB.methodB()

adapter = ImplementationBAdapter()
adapter.methodA()