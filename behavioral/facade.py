
class Subsystem1:
    def operation1(self) -> str:
        return "Subsystem1: Ready!"

class Subsystem2:
    def operation2(self) -> str:
        return "Subsystem2: Go!"

class Facade:

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        self.subsystem1 = subsystem1
        self.subsystem2 = subsystem2

    def operation(self) -> str:
        results = []
        results.append(self.subsystem1.operation1())
        results.append(self.subsystem2.operation2())
        return "\n".join(results)

if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    print(facade.operation())
