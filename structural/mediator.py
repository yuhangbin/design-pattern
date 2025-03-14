from abc import ABC


class Mediator(ABC):

    def notify(self, sender: object, event: str) -> None:
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1: 'Component1') -> None:
        self.component1 = component1
        self.component1.mediator = self
    
    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator handle event A")

class BaseComponent:

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator
    
    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component 1 does A.")
        self.mediator.notify(self, "A")


if __name__ == "__main__":
    c1 = Component1()
    mediator = ConcreteMediator(c1)

    c1.do_a()
