
from abc import ABC, abstractmethod


class ProfileIterator(ABC):

    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def get_next(self) -> 'ProfileIterator':
        pass

class FacebookIterator(ProfileIterator):
    # using linkedlist to store iterator
    def __init__(self, data: list[dict], profileId: str) -> None:
        self.data = data
        self.profileId = profileId

    def has_next(self) -> bool:
        return len(self.data) > 0
    
    def get_next(self) -> 'ProfileIterator':
        return self.data.pop(0)
    

if __name__ == "__main__":
    facebook = FacebookIterator([{"name": "John", "age": 20}, {"name": "Jane", "age": 21}], "123")
    while facebook.has_next():
        print(facebook.get_next());
