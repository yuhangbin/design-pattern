
from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass

class SimpleCommand(Command):

    def __init__(self, payload: str) -> None:
        self.payload = payload

    def execute(self) -> None:
        return (f"Simple Command executing" f"{self.payload}")
    
class ComplexCommand(Command):

    def __init__(self, receiver: 'Receiver', a: str, b: str) -> None:
        self.receiver = receiver
        self.a = a
        self.b = b

    def execute(self) -> None:
        return (f"ComplexCommand: " f"{self.receiver.do_something(self.a)}" f"{self.receiver.do_something_else(self.b)}")
    
class Receiver:

    def do_something(self, a: str) -> None:
        return (f"Receiver: Working on ({a}.)")
    
    def do_something_else(self, b: str) -> None:
        return (f"Receiver: Also working on ({b}.)")

class Invoker:

    def __init__(self, on_start: Command, on_finish: Command) -> None:
        self.on_start = on_start
        self.on_finish = on_finish

    def set_on_start(self, command: Command) -> None:
        self.on_start = command

    def set_on_finish(self, command: Command) -> None:
        self.on_finish = command
        
    def do_something_important(self) -> None:
        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self.on_start, Command):
            self.on_start.execute()

        print("Invoker: ...doing something really important...")
        
        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self.on_finish, Command):
            self.on_finish.execute()

if __name__ == "__main__":
    invoker = Invoker(
        SimpleCommand("Say Hi!"),
        ComplexCommand(
            Receiver(),
            "Send email",
            "Save report"
        )
    )
    invoker.do_something_important()