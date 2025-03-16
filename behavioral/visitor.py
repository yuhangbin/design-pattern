
from abc import ABC, abstractmethod
from os import name


class Shape(ABC):
    @abstractmethod
    def accept(v: 'Visitor'):
        pass

class Dot(Shape):
    def accept(v: 'Visitor'):
        return v.visitDot()

class Visitor(ABC):
    
    @abstractmethod
    def visitDot(d: Dot):
        pass

class XMLExportVisitor(Visitor):

    def visitDot(self, d: Dot):
        print('visitDot')


if __name__ == '__main__':

    visitor = XMLExportVisitor()

    shape = Dot()

    visitor.visitDot(shape)