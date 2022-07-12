from abc import ABC, abstractmethod
import time

class AbstractProductA(ABC):
    @abstractmethod
    def purchase(self):
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def purchase(self):
        pass

class ProductA1(AbstractProductA):
    def purchase(self):
        print("Purchasing product A1...")
        time.sleep(3)
        print("Purchase complete!\n")

class ProductA2(AbstractProductA):
    def purchase(self):
        print("Purchasing product A2...")
        time.sleep(3)
        print("Purchase complete!\n")
    
class ProductB1(AbstractProductA):
    def purchase(self):
        print("Purchasing product B1...")
        time.sleep(3)
        print("Purchase complete!\n")

class ProductB2(AbstractProductA):
    def purchase(self):
        print("Purchasing product B2...")
        time.sleep(3)
        print("Purchase complete!\n")

class ChiefAbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

class ConcreteProductCreator1(ChiefAbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ProductB1()

class ConcreteProductCreator2(ChiefAbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ProductB2()

def code_implementation(FactoryClass: ChiefAbstractFactory) -> None:
    ProductA = FactoryClass.create_product_a()
    ProductB = FactoryClass.create_product_b()

    ProductA.purchase()
    ProductB.purchase()

if __name__ == "__main__":
    print("Test code implementation with the first factory: ")
    code_implementation(ConcreteProductCreator1())

    print("Test code implementation with the second factory: ")
    code_implementation(ConcreteProductCreator2())