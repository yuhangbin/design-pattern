from abc import ABC, abstractmethod
from datetime import datetime
import random
import string
class Originator:

    _state = None
    def __init__(self, state: str) -> None:
        self._state = state

    def do_something(self) -> None:
        print("Something important and change state")
        self._state = self._generate_random_string(30)

    def _generate_random_string(self, length: int = 10) -> str:
        return ''.join(random.sample(string.ascii_letters, length))

    def save(self) -> 'Memento':
        return ConcreteMemento(self._state)
    
    def restore(self, memento: 'Memento') -> None:
        self._state = memento.get_state()
        

class Memento(ABC):

    @abstractmethod
    def get_state(self) -> str:
        pass

class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = datetime.now()

    def get_state(self) -> str:
        return self._state

    def get_date(self) -> str:
        return self._date

class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("Caretaker: saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not self._mementos:
            return
        memento = self._mementos.pop()
        print("Caretaker: restoring state to: " + memento.get_state())
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()
        

if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)


    caretaker.backup()
    originator.do_something()
    caretaker.backup()
    originator.do_something()
    caretaker.backup()
    originator.do_something()

    print(originator._state)

    caretaker.undo()
    print(originator._state)
    