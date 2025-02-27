
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()

class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self):
        pass

class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self):
        return "The result of the product A1"

class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self):
        return "The result of the product A2"

class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self):
        pass

class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self):
        return "The result of the product B1"

class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self):
        return "The result of the product B2"

def client_code(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(product_a.useful_function_a())
    print(product_b.useful_function_b())


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    factory1 = ConcreteFactory1()
    client_code(factory1)
    print("\n")
    print("Client: Testing the same client code with the second factory type:")
    factory2 = ConcreteFactory2()
    client_code(factory2)
    
    