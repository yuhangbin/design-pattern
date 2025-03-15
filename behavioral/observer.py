
from abc import ABC, abstractmethod
import random
import string


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: 'Observer') -> None:
        pass
    
    @abstractmethod
    def detach(self, observer: 'Observer') -> None:
        pass
    
    @abstractmethod
    def notify(self) -> None:
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class ConcreteSubject(Subject):
    def __init__(self) -> None:
        self._state = None
        self._observers = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        print("\nSubject: I'm doing something important.")
        self._state = self._generate_random_string(30)
        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()

    def _generate_random_string(self, length: int = 10) -> str:
        return ''.join(random.sample(string.ascii_letters, length))


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if len(subject._state) < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if len(subject._state) == 0 or len(subject._state) >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    subject = ConcreteSubject()
    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()

    subject.attach(observer_a)
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()
