
class Graphic:
    def move(self, x: int, y: int) -> None:
        pass

    def draw(self) -> None:
        pass

class Dot(Graphic):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def move(self, x: int, y: int) -> None:
        self.x += x 
        self.y += y

    def draw(self) -> None:
        print(f"Dot at ({self.x}, {self.y})")
        
class Circle(Dot):
    def __init__(self, x: int, y: int, radius: int) -> None:
        super().__init__(x, y)
        self.radius = radius
        
    def draw(self) -> None:
        print(f"Circle at ({self.x}, {self.y}) with radius {self.radius}")
        
class CompoundGraphic(Graphic):
    def __init__(self) -> None:
        self.children: list[Graphic] = []
    
    def add(self, child: Graphic) -> None:
        self.children.append(child)
        
    def remove(self, child: Graphic) -> None:
        self.children.remove(child)
    
    def move(self, x: int, y: int) -> None:
        for child in self.children:
            child.move(x, y)
            
    def draw(self) -> None:
        for child in self.children:
            child.draw()
    
class ImageEditor:
    def __init__(self, all_graphics: CompoundGraphic) -> None:
        self.all_graphics = all_graphics
        
    def load(self) -> None:
        self.all_graphics.add(Dot(1, 2))
        self.all_graphics.add(Circle(5, 3, 10))
    
    def group_selected(self, components: list[Graphic]) -> None:
        group = CompoundGraphic()
        for component in components:
            group.add(component)
        self.all_graphics.add(group)
        print("Grouped all components.")
    
if __name__ == "__main__":
    all_graphics = CompoundGraphic()
    editor = ImageEditor(all_graphics)
    editor.load()
    editor.group_selected([Dot(1, 2), Circle(5, 3, 10)])
    editor.all_graphics.draw()
