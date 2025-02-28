from abc import ABC, abstractmethod
import copy
# Base prototype class
class Shape(ABC):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def clone(self):
        pass

    def __str__(self):
        return f"Shape(x={self.x}, y={self.y}, color={self.color})"

class Circle(Shape):
    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color)
        self.radius = radius
        
    def clone(self):
        return copy.copy(self)

    # def deep_clone(self):
    #     return copy.deepcopy(self)
    
    def __str__(self):
        return f"Circle(x={self.x}, y={self.y}, color={self.color}, radius={self.radius})"
    
class Square(Shape):
    def __init__(self, x, y, color, side):
        super().__init__(x, y, color)
        self.side = side

    # shallow clone 
    def clone(self):
        return copy.copy(self)    
    
    # # deep clone 
    # def deep_clone(self):
    #     return copy.deepcopy(self)
    
    def __str__(self):
        return f"Square(x={self.x}, y={self.y}, color={self.color}, side={self.side})"
    

def main():
    circle = Circle(10, 10, "red", 5)
    square = Square(10, 10, "blue", 5)
    print(f"Circle: {circle}")
    print(f"Square: {square}")
    circle_clone = circle.clone()
    square_clone = square.clone()
    
    print(f"Circle clone: {circle_clone}")
    print(f"Square clone: {square_clone}")
    circle_clone.radius = 100
    square_clone.side = 100
    print(f"Circle clone: {circle_clone}")
    print(f"Square clone: {square_clone}")
    print(f"Circle: {circle}")
    print(f"Square: {square}")

if __name__ == "__main__":
    main()