
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self) -> None:
        self.base_operation1()
        self.hook1()
        self.required_operations()
        self.hook2()
        self.base_operation2()
        
    def base_operation1(self) -> None:
        pass
    
    def base_operation2(self) -> None:
        pass
    
    @abstractmethod
    def required_operations(self) -> None:
        pass

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass

class ConcreteClass(AbstractClass):
    def required_operations(self) -> None:
        print("ConcreteClass says: Implemented Operation1")
        print("ConcreteClass says: Implemented Operation2")

    def hook1(self) -> None:
        print("ConcreteClass says: Overridden Hook1")

    def hook2(self) -> None:
        print("ConcreteClass says: Overridden Hook2")


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    ConcreteClass().template_method()

    print("\nSame client code can work with different subclasses:")
    ConcreteClass().template_method()
