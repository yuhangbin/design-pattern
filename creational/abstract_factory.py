
from abc import ABC, abstractmethod


class GUIFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

class WindowsFactory(GUIFactory):
    def create_product_a(self):
        return WindowsButton()

    def create_product_b(self):
        return WindowsCheckBox()

class MacOSFactory(GUIFactory):
    def create_product_a(self):
        return MacOSButton()

    def create_product_b(self):
        return MacOSCheckBox()

class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class WindowsButton(Button):
    def click(self):
        return "Windows button clicked"

class MacOSButton(Button):
    def click(self):
        return "MacOS button clicked"

class CheckBox(ABC):
    @abstractmethod
    def click(self):
        pass

class WindowsCheckBox(CheckBox):
    def click(self):
        return "Windows checkbox clicked"

class MacOSCheckBox(CheckBox):
    def click(self):
        return "MacOS checkbox clicked"

def client_code(factory: GUIFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(product_a.click())
    print(product_b.click())


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    factory1 = WindowsFactory()
    client_code(factory1)
    print("\n")
    print("Client: Testing the same client code with the second factory type:")
    factory2 = MacOSFactory()
    client_code(factory2)
    
    