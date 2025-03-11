from abc import ABC, abstractmethod


class Handler(ABC):

    def __init__(self):
        self.next_handler = None

    def setNext(self, handler: 'Handler') -> 'Handler':
        self.next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request: str) -> str:
        if self.next_handler:
            self.next_handler.handle(request)
    
class ConcreteHandler1(Handler):
    def handle(self, request: str) -> str:
        if request == "1":
            print(f"ConcreteHandler1 handled request {request}")
        else:
            super().handle(request)
        
class ConcreteHandler2(Handler):
    def handle(self, request: str) -> str:
        if request == "2":
            print(f"ConcreteHandler2 handled request {request}")
        else:
            super().handle(request)

class ConcreteHandler3(Handler):
    def handle(self, request: str) -> str:
        if request == "3":
            print(f"ConcreteHandler3 handled request {request}")
        else:
            super().handle(request)

if __name__ == "__main__":
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler3 = ConcreteHandler3()

    handler1.setNext(handler2).setNext(handler3)
    
    handler1.handle("1")
    handler1.handle("2")
    handler1.handle("3")
    handler1.handle("4")
